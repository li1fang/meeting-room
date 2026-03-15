#!/usr/bin/env python3
import re
import sys
from pathlib import Path
import yaml

root = Path(__file__).resolve().parents[1]
name_pat = re.compile(r"^[a-z]+\.[a-z0-9_]+(\.[a-z0-9_]+)?\.v[0-9]+(\.[0-9]+)?$")


def load_yaml(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def err(msg):
    print(f"[ERROR] {msg}")
    return 1


def main():
    rc = 0
    genesis = load_yaml(root / 'genesis.contracts.yaml')
    registry = load_yaml(root / 'common/registry/topics.yaml')

    for domain in genesis.get('domains', []):
        for topic in domain.get('topics', []):
            name = topic['name']
            if not name_pat.match(name):
                rc |= err(f'非法主题名: {name}')
            if name not in registry:
                rc |= err(f'registry 缺主题: {name}')
            schema_path = root / 'schemas' / domain['name'] / f'{name}.schema.json'
            sample_path = root / 'samples' / name / 'minimal.json'
            suite_path = root / 'tck' / 'suites' / domain['name'] / f'{name}.json'
            if not schema_path.exists():
                rc |= err(f'缺 schema: {schema_path}')
            if not sample_path.exists():
                rc |= err(f'缺 sample: {sample_path}')
            if not suite_path.exists():
                rc |= err(f'缺 suite: {suite_path}')

    for name in registry.keys():
        if name not in {t['name'] for d in genesis.get('domains', []) for t in d.get('topics', [])}:
            rc |= err(f'registry 中存在未注册 topic: {name}')

    if rc == 0:
        print('[OK] genesis / registry / files are consistent')
    sys.exit(rc)


if __name__ == '__main__':
    main()
