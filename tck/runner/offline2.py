#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, sys, glob, os
from pathlib import Path

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    suites_dir = sys.argv[1] if len(sys.argv) > 1 else "tck/suites"
    try:
        from tck.runner.jsonpath_assert import eval_expr
    except Exception:
        sys.path.append("tck/runner")
        from jsonpath_assert import eval_expr

    suite_files = glob.glob(os.path.join(suites_dir, "**/*.json"), recursive=True)
    if not suite_files:
        print("[TCK] No suites found."); return 0

    fails = 0; total = 0
    for sf in suite_files:
        try:
            suite = load_json(sf)
        except Exception as e:
            print(f"[FAIL] suite load error: {sf}: {e}"); fails += 1; continue
        for c in suite.get("cases", []):
            total += 1
            name = c.get("name", Path(sf).stem)
            given = c.get("given")
            asserts = c.get("assert_jsonpath", [])
            try:
                data = load_json(given)
            except Exception as e:
                print(f"[FAIL] {name}: unable to load sample {given}: {e}"); fails += 1; continue
            local_fails = 0
            for ex in asserts:
                ok, msg = eval_expr(data, ex)
                if ok:
                    print(f"[PASS] {name}: {msg}")
                else:
                    print(f"[FAIL] {name}: {msg}")
                    local_fails += 1
            if local_fails == 0 and not asserts:
                print(f"[PASS] {name}: loaded")
            fails += local_fails
    if fails:
        print(f"[TCK] FAILED: {fails} failing assertion(s) across {total} case(s).")
        sys.exit(1)
    print(f"[TCK] OK: {total} case(s) checked.")
    return 0

if __name__ == "__main__":
    main()
