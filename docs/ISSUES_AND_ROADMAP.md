# Issues and Roadmap (v3)

## Current repository issues

### 1. Interaction baseline is still the only stable baseline

Current `v1.2` interaction line is the most mature contract line in the repository.
Other lines now exist, but they are still draft extensions.

### 2. Estimation is now useful, but still intentionally bounded

The repository now carries:

- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`
- `naturalcontrol.estimation_observation.v1.1`
- `naturalcontrol.estimation_prediction.v1.1`
- `naturalcontrol.estimation_observation.v1.2`
- `naturalcontrol.estimation_prediction.v1.2`

Current recommendation:

- `naturalcontrol.estimation_observation.v1.2`
- `naturalcontrol.estimation_prediction.v1.2`

What is still missing later:

- ballistic schemas
- heatmap schemas
- RL feedback schemas
- full 3D world/body-space standards
- richer uncertainty standards beyond the current small model

### 3. Actuation now has explicit execution receipt ownership

The repository now carries:

- `naturalcontrol.actuation_bundle.v1`
- `naturalcontrol.actuation_bundle.v1.1`
- `naturalcontrol.actuation_receipt.v1`
- `naturalcontrol.actuation_adapter_receipt.v1`
- `naturalcontrol.actuation_injector_receipt.v1`
- `naturalcontrol.actuation_device_receipt.v1`

Current recommendation:

- `naturalcontrol.actuation_bundle.v1.1`
- `naturalcontrol.actuation_adapter_receipt.v1`
- `naturalcontrol.actuation_injector_receipt.v1`
- `naturalcontrol.actuation_device_receipt.v1`

What is still missing later:

- adapter-specific protocol schemas
- injector-specific packet schemas
- richer touch/gamepad/gear vocabularies
- device-specific low-level protocol schemas

### 4. NP / PS / TS remain reserved only

This is still intentional.
The repository defines how those domains may land later, but it does not yet carry active schemas for them.

### 5. No compatibility layer for legacy AGI-Nutshell

This remains an explicit choice.
It keeps the repository clean, but migration adapters may still be needed later at implementation boundaries.

## Roadmap

### Phase 1 — Land NC interaction baseline

Status: landed

- `naturalcontrol.interaction_request.v1.2`
- `naturalcontrol.interaction_frame.v1.2`
- `naturalcontrol.interaction_trace_pack.v1.2`

### Phase 2 — Land NC lifecycle/reporting line

Status: landed

- `naturalcontrol.lifecycle_ack.v1`
- `naturalcontrol.lifecycle_progress.v1`
- `naturalcontrol.lifecycle_result.v1`

### Phase 3 — Land estimation seed and early draft lines

Status: landed

Seed skeleton:

- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`

Reference draft:

- `naturalcontrol.estimation_observation.v1.1`
- `naturalcontrol.estimation_prediction.v1.1`

### Phase 4 — Land estimation v1.2 tightening

Status: landed

Current recommended draft:

- `naturalcontrol.estimation_observation.v1.2`
- `naturalcontrol.estimation_prediction.v1.2`

Focused gains:

- structured uncertainty
- confidence-level field
- optional 3D expression tightened into structured objects

### Phase 5 — Land actuation seed and bundle draft lines

Status: landed

Seed skeleton:

- `naturalcontrol.actuation_bundle.v1`

Reference draft:

- `naturalcontrol.actuation_bundle.v1.1`
- `naturalcontrol.actuation_receipt.v1`

### Phase 6 — Land execution receipt split

Status: landed

Current recommended execution receipt line:

- `naturalcontrol.actuation_adapter_receipt.v1`
- `naturalcontrol.actuation_injector_receipt.v1`
- `naturalcontrol.actuation_device_receipt.v1`

### Phase 7 — Freeze body keypoint catalog

Status: landed as document-level canonical catalog

- `docs/NC-BODY-KEYPOINT-CATALOG-v1.md`

### Phase 8 — Freeze reserved domain expansion rules

Status: landed as governance rule

- canonical placement for future domains
- minimum landing requirements
- NC-first repository identity preserved

### Phase 9 — Later extensions

Future work may formalize:

- richer 3D and body-space semantics
- ballistic and horizon-specific prediction models
- adapter/injector-specific protocol schemas
- active NP / PS / TS schema lines
