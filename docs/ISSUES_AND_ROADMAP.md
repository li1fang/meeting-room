# Issues and Roadmap (v2)

## Current repository issues

### 1. Interaction baseline is still the only stable baseline

Current `v1.2` interaction line is the most mature contract line in the repository.
Other lines now exist, but they are still draft extensions.

### 2. Estimation now has a recommended line, but it is still early

The repository now carries:

- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`
- `naturalcontrol.estimation_observation.v1.1`
- `naturalcontrol.estimation_prediction.v1.1`

What is still missing later:

- richer uncertainty structures
- optional full 3D coordinate formalization
- ballistic or RL-related semantics
- broader body-keypoint coverage

### 3. Actuation now has a recommended line, but it is still early

The repository now carries:

- `naturalcontrol.actuation_bundle.v1`
- `naturalcontrol.actuation_bundle.v1.1`
- `naturalcontrol.actuation_receipt.v1`

What is still missing later:

- device-specific payload refinement
- adapter or injector-side schemas
- richer touch/gamepad/gear vocabularies
- deeper execution feedback lines

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

### Phase 3 — Land estimation skeleton and recommended draft

Status: landed

Seed skeleton:

- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`

Current recommended draft:

- `naturalcontrol.estimation_observation.v1.1`
- `naturalcontrol.estimation_prediction.v1.1`

### Phase 4 — Land actuation skeleton and recommended draft

Status: landed

Seed skeleton:

- `naturalcontrol.actuation_bundle.v1`

Current recommended draft:

- `naturalcontrol.actuation_bundle.v1.1`
- `naturalcontrol.actuation_receipt.v1`

### Phase 5 — Freeze body keypoint catalog

Status: landed as document-level canonical catalog

- `docs/NC-BODY-KEYPOINT-CATALOG-v1.md`

### Phase 6 — Freeze reserved domain expansion rules

Status: landed as governance rule

- canonical placement for future domains
- minimum landing requirements
- NC-first repository identity preserved

### Phase 7 — Later extensions

Future work may formalize:

- richer 3D and body-space semantics
- ballistic and horizon-specific prediction models
- deeper actuation and device-execution lines
- active NP / PS / TS schema lines
