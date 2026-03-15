# Roadmap Status

Current mainline view of the formal work tracked in the repository.

## Current status

### Interaction baseline

Status: landed

What now exists:

- `naturalcontrol.interaction_request.v1.2`
- `naturalcontrol.interaction_frame.v1.2`
- `naturalcontrol.interaction_trace_pack.v1.2`

Interpretation:

The repository has a stable 2D interaction baseline for request, frame, and trace semantics.

### Lifecycle/reporting line

Status: landed

What now exists:

- `naturalcontrol.lifecycle_ack.v1`
- `naturalcontrol.lifecycle_progress.v1`
- `naturalcontrol.lifecycle_result.v1`

Interpretation:

Interaction semantics and reporting semantics stay separated.

### Estimation line

Status: landed with `v1.2` as current recommended draft

What now exists:

- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`
- `naturalcontrol.estimation_observation.v1.1`
- `naturalcontrol.estimation_prediction.v1.1`
- `naturalcontrol.estimation_observation.v1.2`
- `naturalcontrol.estimation_prediction.v1.2`

Interpretation:

The repository now has a tightened estimation line that freezes structured uncertainty and optional 3D expression while keeping earlier drafts as seed/reference lines.

### Actuation handoff line

Status: landed as current recommended handoff line

What now exists:

- `naturalcontrol.actuation_bundle.v1`
- `naturalcontrol.actuation_bundle.v1.1`
- `naturalcontrol.actuation_adapter_bundle.v1`
- `naturalcontrol.actuation_injector_batch.v1`
- `naturalcontrol.actuation_receipt.v1`
- `naturalcontrol.actuation_adapter_receipt.v1`
- `naturalcontrol.actuation_injector_receipt.v1`
- `naturalcontrol.actuation_device_receipt.v1`

Interpretation:

The repository now makes the handoff between adapter and injector explicit instead of jumping directly from bundle semantics to receipt semantics.

### Reserved domain expansion path

Status: unchanged and still landed as repository rule

What now exists:

- canonical placement rule for future domains
- minimum landing requirements for non-NC domains
- explicit reserved-path document

Interpretation:

The repository stays NC-first while keeping future NP/PS/TS growth disciplined.

### Pause point

Status: active

What now exists:

- `docs/PAUSE_POINT_HANDOFF_v1.md`
- handoff line landed before any deeper protocol work

Interpretation:

The repository now has a defined stopping point where adapter/injector production work can begin without forcing premature backend-specific contract design.

## Mainline view

The current mainline of `meeting-room` is now:

1. NC interaction baseline (`request/frame/trace`)
2. NC lifecycle/reporting line
3. NC estimation line (`v1.2` recommended, `v1.1` retained as reference, `v1` retained as skeleton seed)
4. NC actuation line (`v1.1` bundle recommended, handoff line landed, split execution receipts recommended)
5. reserved multi-domain expansion path
6. active pause point after handoff landing

## Current recommendation

Do not widen scope beyond the current handoff pause point until at least one production pull exists from:

- a real adapter needing richer translation semantics
- a real injector needing explicit packet/protocol contracts
- a cross-team integration that exposes a missing minimum semantic in the current handoff or receipt chain
