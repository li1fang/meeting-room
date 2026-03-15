# NC Lifecycle and Reporting Line v1

Status: Draft

## Purpose

This document defines the first lifecycle/reporting line for `meeting-room`.
It exists to separate runtime execution reporting from the interaction baseline.

The interaction baseline already formalizes:

- request
- frame
- trace pack

Those payloads describe what interaction is requested, what alignment frames look like, and what trace/audit data looks like.
They should not also carry the entire execution lifecycle surface.

## New line

This repository adds three lifecycle/reporting payloads:

- `naturalcontrol.lifecycle_ack.v1`
- `naturalcontrol.lifecycle_progress.v1`
- `naturalcontrol.lifecycle_result.v1`

These are the successor direction for the old idea of `ack/progress/result`, but they are rebuilt under the new formal repository rules.

## Design position

### What belongs here

Belongs in lifecycle/reporting:

- admission / acceptance / start signals
- in-flight execution stage reporting
- terminal execution state
- references to produced artifacts
- runtime execution identifiers

### What does not belong here

Does not belong in lifecycle/reporting:

- action target geometry
- zone map policy
- target snapshots
- emitted cursor trace
- replay payload itself

Those remain in the interaction baseline.

## Shared identifiers

The lifecycle line uses these identifiers:

- `request_id`
- `interaction_id`
- `execution_id`
- optional `trace_id`

### Meaning

- `request_id`: request-side identity
- `interaction_id`: interaction-level identity shared with the baseline
- `execution_id`: runtime execution attempt identity
- `trace_id`: reference to the resulting trace/audit package when available

## Payload roles

### `naturalcontrol.lifecycle_ack.v1`

Use for:

- received
- accepted
- started

This topic confirms admission and the start of a concrete execution attempt.
`execution_id` becomes required when the state reaches `started`.

### `naturalcontrol.lifecycle_progress.v1`

Use for runtime reporting while execution is active.

Current v1 fields:

- `stage`
- `status`
- optional `progress_ratio`
- optional `trace_id`

This topic is not the interaction frame stream.
It is a reporting channel about execution state.

### `naturalcontrol.lifecycle_result.v1`

Use for terminal execution state.

Current v1 fields:

- `terminal_state`
- optional `trace_id`
- `summary`
- optional `error`
- optional artifact references

This closes the lifecycle/reporting line without redefining the trace pack itself.

## Current stage vocabulary

Current `stage` values:

- `intake`
- `planning`
- `executing`
- `emitting`
- `settling`
- `finalizing`

Current `status` values:

- `running`
- `blocked`
- `retrying`
- `degraded`

Current `terminal_state` values:

- `succeeded`
- `failed`
- `aborted`

These are intentionally small for v1.

## Why this line matters

Without a separate lifecycle/reporting line, the repository would drift back into mixing:

- interaction semantics
- runtime progress semantics
- terminal reporting semantics

That was one of the core problems in the older NC surfaces.
This line prevents that regression.

## Future refinement directions

Later refinements may add:

- richer execution attempt metadata
- retry lineage
- explicit blocked/dependency reasons
- stable artifact reference shapes
- orchestrator-facing reporting fields

But the first step is simply to keep lifecycle/reporting separate from request/frame/trace.
