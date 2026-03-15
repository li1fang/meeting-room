# NC Estimation Layer v1.1

Status: Draft

## Purpose

This document defines the next estimation draft line for `meeting-room`.
It deepens the existing `v1` skeleton without mutating the original seed topics in place.

The estimation layer continues to own:

- observed subject state
- predicted future subject state
- confidence and uncertainty facts
- richer tracking and representation semantics

It still does not own:

- action-target intent planning
- zone or rollback policy
- execution bundle semantics
- lifecycle admission/progress/result reporting

## Versioning position

The repository now carries two estimation levels:

- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`

These remain the first skeleton seed.

The current recommended estimation draft line becomes:

- `naturalcontrol.estimation_observation.v1.1`
- `naturalcontrol.estimation_prediction.v1.1`

This repository intentionally uses a new topic name for the richer line instead of mutating `v1` in place.

## New semantics in v1.1

Compared with the v1 skeleton, v1.1 adds:

- explicit `track_state`
- explicit `representation_kind`
- structured `geometry_2d` / `geometry_3d`
- structured `kinematics_2d` / `kinematics_3d`
- a small canonical body-keypoint catalog
- simple `uncertainty` for prediction
- `source_ref` and `model_ref` fields for traceability

## Payload roles

### `naturalcontrol.estimation_observation.v1.1`

Use for current observed subject state.

Required top-level fields:

- `schema_id`
- `spec_version`
- `epoch_ns`
- `observation_id`
- `coordinate_space`
- `subjects[]`

Each subject carries:

- `subject_id`
- `kind`
- `track_state`
- `confidence`
- `representation_kind`

Each subject may additionally carry:

- `geometry_2d.bbox`
- `geometry_2d.point`
- optional `geometry_3d.position`
- optional `kinematics_2d`
- optional `kinematics_3d`
- optional `body_keypoint_set`
- optional `body_keypoints[]`
- optional `source_ref`

### `naturalcontrol.estimation_prediction.v1.1`

Use for future predicted subject state.

Required top-level fields:

- `schema_id`
- `spec_version`
- `epoch_ns`
- `prediction_id`
- `source_observation_id`
- `horizon_ns`
- `coordinate_space`
- `subjects[]`

Each predicted subject carries:

- `subject_id`
- `confidence`
- `representation_kind`
- `uncertainty`

Each predicted subject may additionally carry:

- `geometry_2d.bbox`
- `geometry_2d.point`
- optional `geometry_3d.position`
- optional `kinematics_2d`
- optional `kinematics_3d`
- optional `body_keypoints[]`
- optional `model_ref`

## Relationship to NP

`meeting-room` remains NC-first.
The estimation layer is still not a direct NP topic line.

This layer defines the NC-side formal boundary for observation and prediction so future NP integration can land against a stable contract surface instead of pushing richer semantics directly into interaction or lifecycle payloads.

## Scope boundary

Current v1.1 freezes:

- 2D observation and prediction baseline
- explicit tracking state
- explicit representation kind
- small canonical body-keypoint vocabulary
- simple uncertainty shape
- optional 3D extension slots

Current v1.1 still does not freeze:

- ballistic prediction
- heatmap schemas
- RL correction surfaces
- covariance or matrix uncertainty standards
- full 3D body-space contracts

## Borrowing stance from AGI-Nutshell

This line borrows only the design direction that richer subject-state expression belongs in its own layer.
It does not absorb old topic names, envelopes, or compatibility rules.

Borrowed idea:

- richer perception/state expression needs a formal home

Not borrowed:

- old topic identity
- old wire shape
- old envelope requirements

## Why this line matters

Without this deeper draft line, the repository would be forced to either:

- keep estimation too weak to be useful, or
- leak richer perception/prediction semantics into interaction or trace payloads

v1.1 avoids both outcomes while preserving the v1 seed.
