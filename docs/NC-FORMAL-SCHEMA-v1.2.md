# NC Formal Schema v1.2

Status: Draft

## Purpose

This document defines the NC formal schema draft line `v1.2`.
It is the first formal baseline for Natural Control in this repository.

`v1.2` freezes the 2D interaction layer first.
It does not attempt to cover all future control modes.

## Payload set

- `naturalcontrol.common.v1.2`
- `naturalcontrol.interaction_request.v1.2`
- `naturalcontrol.interaction_frame.v1.2`
- `naturalcontrol.interaction_trace_pack.v1.2`

## Accepted core semantics

- `schema_id + spec_version + epoch_ns`
- explicit `coordinate_space`
- `action_targets[]` with `bbox` as required geometry
- explicit `zone_map`
- plural `cluster_hint_refs`
- structured `rollback_actions`
- `request_snapshot` in trace packs
- `position + delta + source_segment` in trace samples
- `zone_map.availability = known|unknown|not_provided`

## Scope

In scope:

- 2D interaction request semantics
- online frame alignment semantics
- offline trace/audit/replay pack semantics
- click / release / drag-like task expression
- event clustering and natural-settle closure
- intelligent-miss starter surface through zones and rollback actions

Out of scope:

- 3D coordinate systems
- body-part heatmaps / pose semantics
- ballistic prediction
- RL feedback contracts
- gear-control / gamepad / touch actuation contracts

## Why this boundary exists

If richer 3D or actuation semantics are forced into the first baseline, the request/frame/trace layer becomes unstable.
The first formal step is to freeze the 2D interaction layer cleanly.

## Future extension direction

Future work should extend in layers:

1. interaction layer
2. estimation layer
3. actuation layer

`v1.2` itself remains layer 1 only.
The repository now also carries separate draft lines for layers 2 and 3, but those do not widen the `v1.2` baseline itself.
