#!/usr/bin/env python3
"""Run from project root; files resolved beside this script, receipts retained there."""
import json, os, pathlib, subprocess, time
here = pathlib.Path(__file__).resolve().parent
root = pathlib.Path.cwd()
compiler = pathlib.Path.home() / '.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean'
pkgs = ['mathlib','batteries','aesop','Qq','proofwidgets','importGraph','LeanSearchClient','plausible','Cli']
env = dict(os.environ, LEAN_PATH=':'.join(str(root/'.lake/packages'/p/'.lake/build/lib/lean') for p in pkgs) + ':' + str(root/'.lake/build/lib/lean'))
for name in ['TargetProbes', 'MathlibComposition']:
    cmd = [str(compiler), str(here/(name+'.lean'))]
    start = time.monotonic()
    r = subprocess.run(cmd, cwd=root, env=env, text=True, capture_output=True, timeout=300)
    (here/(name+'.log')).write_text(r.stdout+r.stderr)
    receipt = dict(command=cmd,cwd=str(root),LEAN_PATH=env['LEAN_PATH'],exit_code=r.returncode,elapsed_seconds=time.monotonic()-start)
    (here/(name+'.receipt.json')).write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt),flush=True)
