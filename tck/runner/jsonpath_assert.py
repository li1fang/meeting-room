#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re

def get(data, path):
    if not path.startswith("$."):
        raise ValueError("path must start with $.")
    cur = data
    tokens = re.findall(r'\.?([A-Za-z0-9_]+)|\[(\d+)\]', path[2:])
    for key, idx in tokens:
        if key:
            cur = cur.get(key) if isinstance(cur, dict) else None
        else:
            di = int(idx)
            if isinstance(cur, list) and len(cur) > di:
                cur = cur[di]
            else:
                cur = None
        if cur is None:
            break
    return cur

def eval_expr(data, expr):
    expr = expr.strip()
    if expr.endswith(" exists"):
        p = expr[:-7].strip()
        return get(data, p) is not None, f"{p} exists"
    m = None
    for op in ["==","!="]:
        m = re.match(r'(.+?)\s*(' + re.escape(op) + r')\s*(.+)$', expr)
        if m:
            p, o, rhs = m.groups()
            rhs = rhs.strip()
            if rhs.startswith("'") and rhs.endswith("'"):
                rhs = rhs[1:-1]
            elif rhs.startswith('"') and rhs.endswith('"'):
                rhs = rhs[1:-1]
            else:
                try:
                    if rhs in ("true","false"):
                        rhs = (rhs=="true")
                    elif rhs == "null":
                        rhs = None
                    else:
                        rhs = json.loads(rhs)
                except Exception:
                    pass
            val = get(data, p.strip())
            return (val == rhs) if o=="==" else (val != rhs), f"{p.strip()} {o} {rhs} (got {val})"
    val = get(data, expr)
    return val not in (None, "", []), f"{expr} non-empty"
