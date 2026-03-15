# meeting-room

Natural Control formal contracts repository.

This repository is the new NC-first contract source of truth.
It starts with the NC `v1.2` formal draft line and keeps the scope intentionally narrow:

- interaction request / frame / trace pack
- lifecycle / reporting line
- supporting governance, registry, terminology, samples, and TCK

It does **not** treat legacy AGI-Nutshell NCv3 as the main line.
Legacy material is referenced only as input for borrowing or migration analysis.

## Current scope

Current formal line:

- `naturalcontrol.interaction_request.v1.2`
- `naturalcontrol.interaction_frame.v1.2`
- `naturalcontrol.interaction_trace_pack.v1.2`
- `naturalcontrol.common.v1.2`
- `naturalcontrol.lifecycle_ack.v1`
- `naturalcontrol.lifecycle_progress.v1`
- `naturalcontrol.lifecycle_result.v1`

Current scope is **2D interaction baseline** only.
Out of scope for this first repository version:

- 3D control / body-space contracts
- ballistic prediction
- gear-control / gamepad / touch actuation contracts
- RL feedback contracts
- compatibility wrappers for legacy NCv3

## Canonical tree

This repository uses one canonical tree only:

- `schemas/nc/`
- `samples/`
- `tck/`
- `docs/`
- `common/registry/`
- `tools/`
- `genesis.contracts.yaml`

No `domains/**` mirror tree exists here.

## Naming and envelope

This repository allows direct minor-version naming for formal draft lines.
Examples:

- `naturalcontrol.interaction_request.v1.2`
- `naturalcontrol.interaction_frame.v1.2`

The NC formal line uses its native top-level identity:

- `schema_id`
- `spec_version`
- `epoch_ns`

It does not inherit the old universal event envelope.

## Repository status

- NC-first: yes
- Stable multi-domain SSOT: not yet
- NP/PS/TS extension slots: reserved, not implemented here in v1

## Validation

Run:

```bash
make check
```

This executes:

- schema/sample validation
- NC TCK suites
- registry and governance lint

## Documents

Start with:

- `docs/NC-FORMAL-SCHEMA-v1.2.md`
- `docs/NC-LIFECYCLE-REPORTING-v1.md`
- `docs/ROADMAP_STATUS.md`
- `docs/NaturalControl_Formal_Terminology_zh_en.md`
- `docs/AGI_Nutshell_Legacy_Inventory.md`
- `docs/MIGRATION_FROM_AGI_NUTSHELL.md`
- `docs/ISSUES_AND_ROADMAP.md`
- `docs/SCHEMA.md`
- `docs/GOVERNANCE.md`
- `CONTRIBUTING.md`
