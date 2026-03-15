#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
import yaml

root = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_yaml(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def main():
    genesis = load_yaml(root / 'genesis.contracts.yaml')
    registry = Registry()
    schema_root = root / 'schemas' / 'nc'
    for path in schema_root.glob('*.json'):
        registry = registry.with_resource(path.name, Resource.from_contents(load_json(path)))

    for domain in genesis.get('domains', []):
        for topic in domain.get('topics', []):
            schema_path = root / 'schemas' / domain['name'] / f"{topic['name']}.schema.json"
            sample_path = root / 'samples' / topic['name'] / 'minimal.json'
            schema = load_json(schema_path)
            sample = load_json(sample_path)
            Draft202012Validator(schema, registry=registry).validate(sample)
            print(f'[OK] {sample_path} -> {schema_path}')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'[ERROR] {exc}')
        sys.exit(1)
