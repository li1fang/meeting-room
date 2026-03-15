# meeting-room

Natural Control formal contracts repository.

This repository is the NC-first contract source of truth.
It starts from the NC `v1.2` formal baseline and then grows in explicit layers:

- interaction request / frame / trace pack
- lifecycle / reporting line
- estimation layer
- actuation layer
- supporting governance, registry, terminology, samples, and TCK

It does **not** treat legacy AGI-Nutshell NCv3 as the main line.
Legacy material is referenced only as input for borrowing or migration analysis.

## Current scope

Current formal lines:

- `naturalcontrol.interaction_request.v1.2`
- `naturalcontrol.interaction_frame.v1.2`
- `naturalcontrol.interaction_trace_pack.v1.2`
- `naturalcontrol.common.v1.2`
- `naturalcontrol.lifecycle_ack.v1`
- `naturalcontrol.lifecycle_progress.v1`
- `naturalcontrol.lifecycle_result.v1`
- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`
- `naturalcontrol.actuation_bundle.v1`

Current stable baseline is still **2D interaction**.
The newer estimation and actuation lines are draft extensions that intentionally stay narrow.

Out of scope for the current repository version:

- frozen 3D control contracts
- ballistic prediction standards
- body-part heatmap standards
- RL feedback contracts
- compatibility wrappers for legacy NCv3
- active NP/PS/TS schema lines

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

The NC formal lines use native top-level identity:

- `schema_id`
- `spec_version`
- `epoch_ns`

They do not inherit the old universal event envelope.

## Repository status

- NC-first: yes
- Interaction baseline: landed
- Lifecycle/reporting line: landed
- Estimation line: landed as draft skeleton
- Actuation line: landed as draft skeleton
- NP/PS/TS extension slots: reserved path only

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
- `docs/NC-ESTIMATION-LAYER-v1.md`
- `docs/NC-ACTUATION-LAYER-v1.md`
- `docs/FUTURE_DOMAIN_EXPANSION_RULES.md`
- `docs/ROADMAP_STATUS.md`
- `docs/NaturalControl_Formal_Terminology_zh_en.md`
- `docs/AGI_Nutshell_Legacy_Inventory.md`
- `docs/MIGRATION_FROM_AGI_NUTSHELL.md`
- `docs/ISSUES_AND_ROADMAP.md`
- `docs/SCHEMA.md`
- `docs/GOVERNANCE.md`
- `CONTRIBUTING.md`
