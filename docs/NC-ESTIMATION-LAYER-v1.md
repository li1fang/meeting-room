# NC Estimation Layer v1

Status: Draft

## Purpose

This document defines the first estimation layer for `meeting-room`.
It formalizes observation and prediction payloads without redefining interaction or actuation semantics.

The estimation layer exists so the repository has a formal home for:

- observed target or subject state
- predicted future target or subject state
- confidence and uncertainty facts
- richer motion facts beyond the 2D interaction baseline

It does not replace:

- `naturalcontrol.interaction_request.v1.2`
- `naturalcontrol.interaction_frame.v1.2`
- `naturalcontrol.interaction_trace_pack.v1.2`
- `naturalcontrol.lifecycle_*`

## New line

This repository adds two estimation payloads:

- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`

These payloads are intentionally minimal in v1.
They provide a stable place to express what is seen now and what is predicted next.

## Design position

### What belongs here

Belongs in estimation:

- observed subject geometry
- observed or inferred motion facts
- confidence attached to observed or predicted state
- future-state prediction horizon
- optional body keypoints or 3D extension fields

### What does not belong here

Does not belong in estimation:

- action-target intent planning
- zone policy or rollback policy
- execution bundles
- lifecycle admission/progress/result reporting

Interaction asks what should happen.
Estimation describes what is seen or predicted.
Actuation describes how execution-side atoms should be emitted.

## Relationship to NP

The repository remains NC-first.
The estimation layer is not a direct NP topic line.
It is the NC-side contract surface that can later consume or align with richer NP outputs.

This means:

- NP may become one producer or reference source later
- NC keeps ownership of the formal estimation boundary in this repository
- no NP schema is added in this round

## Payload roles

### `naturalcontrol.estimation_observation.v1`

Use for current observed state.

Current v1 minimums:

- `observation_id`
- `coordinate_space`
- `subjects[]`

Each subject can carry:

- `bbox2d` or `point2d`
- optional `position3d`
- optional `velocity`
- optional `acceleration`
- optional `body_keypoints`
- `confidence`

### `naturalcontrol.estimation_prediction.v1`

Use for future predicted state.

Current v1 minimums:

- `prediction_id`
- `source_observation_id`
- `horizon_ns`
- `subjects[]`

Each predicted subject can carry:

- future `bbox2d` or `point2d`
- optional `position3d`
- optional `velocity`
- optional `acceleration`
- optional `uncertainty`
- optional `model_ref`
- `confidence`

## Scope boundary

Current v1 only freezes:

- 2D observation and prediction baseline
- optional 3D extension slots
- subject-level geometry and motion facts

Current v1 does not freeze:

- ballistic prediction
- body-part heatmaps
- RL correction surfaces
- covariance matrix standards
- full 3D body-space contracts

Those remain future work.

## Borrowing stance from AGI-Nutshell

This line borrows only design direction from older work such as richer perception and state expression.
It does not absorb old topic names, envelopes, or compatibility constraints.

Borrowed idea:

- richer subject-state expression deserves its own formal layer

Not borrowed:

- old topic identity
- old wire shape
- old envelope requirements

## Why this line matters

Without a separate estimation layer, the repository would drift into forcing prediction or perception semantics into:

- interaction request payloads
- interaction frames
- trace packs

That would destabilize the baseline.
This line prevents that.

## Future refinement directions

Later refinements may add:

- stable body-keypoint catalogs
- richer uncertainty structures
- 3D coordinate-space standards
- body-part semantic regions
- ballistic or horizon-specific prediction models

The first step is only to create a clean formal layer for observation and prediction.
