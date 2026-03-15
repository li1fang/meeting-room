# NC Estimation Layer v1.2

Status: Draft

## Purpose

This document defines the next estimation draft line for `meeting-room`.
It tightens the `v1.1` line in two places:

- uncertainty shape
- optional 3D expression

The repository continues to keep older lines unchanged:

- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`
- `naturalcontrol.estimation_observation.v1.1`
- `naturalcontrol.estimation_prediction.v1.1`

The current recommended estimation draft line becomes:

- `naturalcontrol.estimation_observation.v1.2`
- `naturalcontrol.estimation_prediction.v1.2`

## What changes in v1.2

Compared with `v1.1`, this line now freezes:

- explicit self-contained optional 3D expression
- explicit uncertainty model
- explicit confidence level for uncertainty
- explicit 2D uncertainty region shape
- optional 3D uncertainty region shape

It still does not freeze:

- ballistic prediction
- heatmap schemas
- RL correction surfaces
- full 3D body-space standards
- covariance-matrix standards

## Optional 3D expression

In `v1.2`, optional 3D expression is no longer just a loose extension slot.
When 3D is used, it must be expressed in structured objects that declare:

- `space_kind`
- `units`
- concrete geometry or kinematics values

This keeps 3D optional while preventing ad hoc payload drift.

Current `space_kind` values for 3D fields:

- `camera_xyz`
- `world_xyz`
- `custom`

Current `units` values for 3D fields:

- `meters`
- `normalized`
- `custom`

## Uncertainty in v1.2

`v1.1` only used a simple scalar radius form.
`v1.2` replaces that with a small structured model.

Prediction uncertainty now carries:

- `model`
- `confidence_level`
- `region_2d`
- optional `region_3d`

Current `model` values:

- `circle2d`
- `ellipse2d`
- `circle2d+sphere3d`
- `ellipse2d+sphere3d`

Current `region_2d.shape` values:

- `circle`
- `ellipse`

Current `region_3d.shape` values:

- `sphere`

This is intentionally still small.
It is stricter than `v1.1`, but it is not yet a full probabilistic standard.

## Scope boundary

Current `v1.2` freezes:

- 2D observation/prediction baseline
- explicit `track_state`
- explicit `representation_kind`
- canonical body-keypoint catalog usage
- self-contained optional 3D expression
- structured uncertainty model

Current `v1.2` still does not freeze:

- ballistic trajectory prediction
- target heatmaps
- RL correction contracts
- covariance matrices
- full 3D world/body-space standards

## Borrowing stance from AGI-Nutshell

This line still borrows only the design direction that richer subject-state expression belongs in its own layer.
It does not absorb old topic names, envelopes, or compatibility rules.

Borrowed idea:

- richer prediction/state expression needs a formal home

Not borrowed:

- old topic identity
- old wire shape
- old envelope requirements
