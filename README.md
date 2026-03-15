# meeting-room

Natural Control formal contracts repository.

This repository is the NC-first contract source of truth.
It starts from the NC `v1.2` interaction baseline and grows in explicit lines:

- interaction request / frame / trace pack
- lifecycle / reporting line
- estimation line
- actuation line
- supporting governance, registry, terminology, samples, and TCK

It does **not** treat legacy AGI-Nutshell NCv3 as the main line.
Legacy material is referenced only as input for borrowing or migration analysis.

## Current scope

Current formal topics in the repository:

- `naturalcontrol.interaction_request.v1.2`
- `naturalcontrol.interaction_frame.v1.2`
- `naturalcontrol.interaction_trace_pack.v1.2`
- `naturalcontrol.common.v1.2`
- `naturalcontrol.lifecycle_ack.v1`
- `naturalcontrol.lifecycle_progress.v1`
- `naturalcontrol.lifecycle_result.v1`
- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`
- `naturalcontrol.estimation_observation.v1.1`
- `naturalcontrol.estimation_prediction.v1.1`
- `naturalcontrol.estimation_observation.v1.2`
- `naturalcontrol.estimation_prediction.v1.2`
- `naturalcontrol.actuation_bundle.v1`
- `naturalcontrol.actuation_bundle.v1.1`
- `naturalcontrol.actuation_receipt.v1`
- `naturalcontrol.actuation_adapter_bundle.v1`
- `naturalcontrol.actuation_injector_batch.v1`
- `naturalcontrol.actuation_adapter_receipt.v1`
- `naturalcontrol.actuation_injector_receipt.v1`
- `naturalcontrol.actuation_device_receipt.v1`

Current stable baseline is still **2D interaction**.
The richer estimation and actuation lines are draft extensions layered on top of that baseline.

Current recommended draft lines:

- estimation: `naturalcontrol.estimation_observation.v1.2` + `naturalcontrol.estimation_prediction.v1.2`
- actuation: `naturalcontrol.actuation_bundle.v1.1` + handoff line (`naturalcontrol.actuation_adapter_bundle.v1`, `naturalcontrol.actuation_injector_batch.v1`) + execution receipts (`naturalcontrol.actuation_adapter_receipt.v1`, `naturalcontrol.actuation_injector_receipt.v1`, `naturalcontrol.actuation_device_receipt.v1`)

Seed skeleton lines retained for reference:

- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`
- `naturalcontrol.actuation_bundle.v1`

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
- `naturalcontrol.estimation_observation.v1.1`
- `naturalcontrol.actuation_bundle.v1.1`

The NC formal lines use native top-level identity:

- `schema_id`
- `spec_version`
- `epoch_ns`

They do not inherit the old universal event envelope.

## Repository status

- NC-first: yes
- Interaction baseline: landed
- Lifecycle/reporting line: landed
- Estimation line: `v1` skeleton retained, `v1.2` recommended draft landed
- Actuation line: `v1` skeleton retained, `v1.1` bundle + handoff line + execution receipts landed
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
- `docs/NC-ESTIMATION-LAYER-v1.1.md`
- `docs/NC-ESTIMATION-LAYER-v1.2.md`
- `docs/NC-BODY-KEYPOINT-CATALOG-v1.md`
- `docs/NC-ACTUATION-LAYER-v1.md`
- `docs/NC-ACTUATION-LAYER-v1.1.md`
- `docs/NC-ACTUATION-HANDOFF-v1.md`
- `docs/NC-ACTUATION-EXECUTION-RECEIPTS-v1.md`
- `docs/FUTURE_DOMAIN_EXPANSION_RULES.md`
- `docs/ROADMAP_STATUS.md`
- `docs/NaturalControl_Formal_Terminology_zh_en.md`
- `docs/AGI_Nutshell_Legacy_Inventory.md`
- `docs/MIGRATION_FROM_AGI_NUTSHELL.md`
- `docs/ISSUES_AND_ROADMAP.md`
- `docs/SCHEMA.md`
- `docs/GOVERNANCE.md`
- `docs/PAUSE_POINT_HANDOFF_v1.md`
- `CONTRIBUTING.md`
