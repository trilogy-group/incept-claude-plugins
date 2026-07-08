#!/usr/bin/env python3
"""Self-contained TimeBack API client — stdlib only, no repo dependencies.

Drop-in for the surface the co-located scripts use from the (optional) alpha-read-packager
helper `push_to_timeback.py`: `mint_token()`, `get_json(url, tok)`, and the base constants.
Auth is the Cognito client-credentials flow documented in SKILL.md §6.1. Credentials come
from env only — never printed, never written anywhere.

Env (the credential bundle uses exactly these names):
  TIMEBACK_SSO_CLIENT_ID / TIMEBACK_SSO_CLIENT_SECRET   (or TIMEBACK_CLIENT_ID/_SECRET)
  TIMEBACK_TOKEN_URL      optional explicit token endpoint (wins over everything)
  TIMEBACK_ISSUER_URL     Cognito issuer (informational; NOT used to derive the token URL —
                          the shipped issuer's JWKS host does not serve /oauth2/token and 400s.
                          The default token endpoint is the amazoncognito.com domain below.)
  TIMEBACK_QTI_BASE / TIMEBACK_OR_BASE                  optional base-URL overrides
"""
import base64, json, os, urllib.error, urllib.parse, urllib.request

QTI = os.environ.get("TIMEBACK_QTI_BASE", "https://qti.alpha-1edtech.ai/api")
OR = os.environ.get("TIMEBACK_OR_BASE", "https://api.alpha-1edtech.ai/ims/oneroster")
CALIPER = "https://caliper.alpha-1edtech.ai/caliper/events"

_DEFAULT_TOKEN_URL = ("https://prod-beyond-timeback-api-2-idp.auth.us-east-1"
                      ".amazoncognito.com/oauth2/token")


def _env(*names):
    for n in names:
        v = os.environ.get(n)
        if v:
            return v
    raise SystemExit("missing env: set one of %s (values never printed)" % "/".join(names))


def _token_url():
    # An explicit TIMEBACK_TOKEN_URL always wins. Otherwise use the known-good
    # amazoncognito.com token endpoint. We deliberately do NOT derive the token URL from
    # TIMEBACK_ISSUER_URL: the shipped issuer is the Cognito JWKS host, which returns HTTP 400
    # on /oauth2/token — the working token endpoint is the .auth.<region>.amazoncognito.com domain.
    return os.environ.get("TIMEBACK_TOKEN_URL") or _DEFAULT_TOKEN_URL


def mint_token():
    """Client-credentials POST against Cognito. Returns (access_token, scopes)."""
    data = urllib.parse.urlencode({
        "grant_type": "client_credentials",
        "client_id": _env("TIMEBACK_CLIENT_ID", "TIMEBACK_SSO_CLIENT_ID"),
        "client_secret": _env("TIMEBACK_CLIENT_SECRET", "TIMEBACK_SSO_CLIENT_SECRET"),
    }).encode()
    r = urllib.request.urlopen(urllib.request.Request(
        _token_url(), data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}), timeout=30)
    tok = json.load(r)["access_token"]
    scopes = json.loads(base64.urlsafe_b64decode(tok.split(".")[1] + "==")).get("scope", "")
    return tok, scopes


def get_json(url, tok):
    """GET with bearer token. Returns (http_status, parsed_json_or_None)."""
    try:
        r = urllib.request.urlopen(urllib.request.Request(
            url, headers={"Authorization": "Bearer " + tok}), timeout=30)
        return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        return e.code, None


def post_json(url, body, tok, method="POST"):
    """POST/PUT a JSON body. Returns (http_status, parsed_json_or_None).
    Note the QTI update path is PUT, not POST (POST to an existing id = 409)."""
    data = json.dumps(body).encode()
    try:
        r = urllib.request.urlopen(urllib.request.Request(
            url, data=data, method=method,
            headers={"Authorization": "Bearer " + tok,
                     "Content-Type": "application/json"}), timeout=40)
        raw = r.read()
        return r.status, (json.loads(raw) if raw else None)
    except urllib.error.HTTPError as e:
        return e.code, None
