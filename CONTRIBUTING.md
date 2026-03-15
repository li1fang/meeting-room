# Contributing

## Working rule

This repository is NC-first and formal-contract-first.
Changes should make the formal contract line clearer, not more compatible with legacy drift.

## Canonical tree

Contribute only through the root canonical tree:

- `schemas/`
- `samples/`
- `tck/`
- `docs/`
- `common/registry/`
- `tools/`
- `genesis.contracts.yaml`

Do not introduce a mirrored `domains/**` tree.

## Topic landing rule

A new topic is not considered landed unless the same change set includes:

1. schema file
2. minimal sample
3. TCK suite
4. registry entry
5. documentation update when semantics change

## Current naming rule

- direct minor-version naming is allowed
- formal draft lines may use names such as `*.v1.2`
- stable and draft lines may coexist

## Current NC envelope rule

The current NC formal line uses:

- `schema_id`
- `spec_version`
- `epoch_ns`

Do not add compatibility wrappers or legacy envelope fallbacks unless they are explicitly approved as a new contract line.

## What not to do

- do not reintroduce legacy NCv3 request semantics as the main NC line
- do not add `domains/**` duplication
- do not make registry entries without matching schema/sample/TCK
- do not force 3D / ballistic / gear-control semantics into the 2D `v1.2` baseline

## Validation

Before submitting changes, run:

```bash
make check
```
