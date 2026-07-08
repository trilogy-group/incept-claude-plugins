#!/usr/bin/env python3
"""Run blind_solve_probe via the TFY gpt-4.1 gateway (cross-family solver).
Passes through all argv to the probe's argparse (so --bundle/--out/--with-passage/--threads work).
Evaluation-only. Requires TFY_API_KEY/TFY_BASE_URL in env."""
import os, sys
sys.path.insert(0, "/Users/stanhus/Documents/grade3-reading/artifacts/alpha-read-packager/generator/g5")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blind_solve_probe as B

B.MODEL = "gpt-4.1"
B.ENDPOINT = os.environ["TFY_BASE_URL"].rstrip("/") + "/openai/chat/completions"
os.environ["OPENAI_API_KEY"] = os.environ["TFY_API_KEY"]

sys.argv = ["run_g5_probe_tfy"] + sys.argv[1:]   # forward args to the probe
B.main()
