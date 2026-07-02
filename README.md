# incept-claude-plugins

Internal Claude Code plugin marketplace for Incept. Distributes reviewer-knowledge-base
skills used by reviewer agents to evaluate course/product approval cases with full context
(design rationale, evidence, honest tradeoffs) rather than a bare checklist.

## Plugins

| Plugin | What it's for |
|---|---|
| `grade3-reading-brainlift` | Reviewer knowledge base for the Grade-3 course `reading-explorers-v2` (TimeBack). |
| `map-proxy-brainlift` | Reviewer knowledge base for the Incept MAP Proxy (G2-G5 adaptive reading CAT vs. NWEA MAP Growth). |

## Install (one-time per user)

```
/plugin marketplace add trilogy-group/incept-claude-plugins
/plugin install grade3-reading-brainlift@incept-claude-plugins
/plugin install map-proxy-brainlift@incept-claude-plugins
```

Or non-interactively:

```bash
claude plugin marketplace add trilogy-group/incept-claude-plugins
claude plugin install grade3-reading-brainlift@incept-claude-plugins
claude plugin install map-proxy-brainlift@incept-claude-plugins
```

Once installed, invoke a plugin's skill directly:

```
/grade3-reading-brainlift:grade3-reading-brainlift
/map-proxy-brainlift:map-proxy-brainlift
```

Claude also auto-loads a skill's description into context and will pull it in on its own
when a task matches (e.g. "review reading-explorers-v2 for approval").

## Auto-suggest for a project's team

Add to that project's `.claude/settings.json` so teammates who trust the folder get
prompted to install this marketplace automatically:

```json
{
  "extraKnownMarketplaces": {
    "incept-claude-plugins": {
      "source": {
        "source": "github",
        "repo": "trilogy-group/incept-claude-plugins"
      }
    }
  },
  "enabledPlugins": {
    "map-proxy-brainlift@incept-claude-plugins": true
  }
}
```

## Updating a skill

Edit the relevant `plugins/<name>/skills/<name>/SKILL.md`, bump `version` in that plugin's
`.claude-plugin/plugin.json` (and in the corresponding entry in
`.claude-plugin/marketplace.json` if you also set it there), commit, and push. Existing
users pick up the change with `/plugin marketplace update`.

## Validate before pushing

```bash
claude plugin validate .
```
