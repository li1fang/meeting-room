# NC Body Keypoint Catalog v1

Status: Draft

## Purpose

This document freezes the first small body-keypoint vocabulary used by the current estimation draft line.
It exists to stop schema examples and future implementations from drifting into ad hoc naming.

This catalog is intentionally small.
It is not a general-purpose pose schema.

## Catalog identity

Catalog name:

- `upper_body_front_v1`

## Canonical keypoints

The initial keypoint set is:

- `head_center`
- `neck_center`
- `left_eye`
- `right_eye`
- `left_shoulder`
- `right_shoulder`

## Intended use

This catalog is currently used by:

- `naturalcontrol.estimation_observation.v1.1`
- `naturalcontrol.estimation_prediction.v1.1`

It provides stable names for optional body-keypoint arrays and optional body-keypoint set declarations.

## Non-goals

This catalog does not yet define:

- full-body pose coverage
- left/right hand or lower-body points
- skeletal edges or topology
- heatmaps
- confidence thresholds
- 3D body-joint standards

Those remain future work.
