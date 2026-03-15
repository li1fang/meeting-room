# NC Actuation Layer v1

Status: Draft

## Purpose

This document defines the first actuation layer for `meeting-room`.
It formalizes execution-side bundles without redefining interaction or lifecycle semantics.

The actuation layer exists so the repository has a formal home for:

- execution bundles
- device-facing atom lists
- mapping from interaction outputs to device surfaces

It does not replace:

- `naturalcontrol.interaction_*`
- `naturalcontrol.lifecycle_*`

## New line

This repository adds one actuation payload:

- `naturalcontrol.actuation_bundle.v1`

This payload is the first formal successor direction for older execution-oriented bundle ideas.
It is intentionally small in v1.

## Design position

### What belongs here

Belongs in actuation:

- execution bundle identity
- device surface kind
- time basis for emitted atoms
- atom list and payloads
- optional mapping references

### What does not belong here

Does not belong in actuation:

- action-target intent planning
- zone policy
- observation or prediction state
- runtime lifecycle reporting

Interaction says what needs to happen.
Actuation says how a device-facing bundle is shaped.
Lifecycle says how execution is admitted, progresses, and ends.

## Payload role

### `naturalcontrol.actuation_bundle.v1`

Use for a device-facing bundle of execution atoms.

Current v1 minimums:

- `bundle_id`
- `request_id`
- `interaction_id`
- `execution_id`
- `surface_kind`
- `time_basis`
- `atoms[]`

Current `surface_kind` values:

- `mouse`
- `touch`
- `gamepad`
- `gear`
- `unknown`

Current atom kinds:

- `pointer_delta`
- `pointer_button`
- `touch_contact`
- `stick_vector`
- `wait`
- `gear_vector`

Each atom carries:

- `atom_id`
- `offset_ns`
- `duration_ns`
- `kind`
- `payload`

Optional fields:

- `coordinate_space`
- `mapping_ref`
- `source_segment`

## Relationship to older execution bundles

This line borrows only the layering idea from older execution-bundle work such as `nc.control.bundle.v1`.
It does not adopt that topic name, payload shape, or old envelope.

Borrowed idea:

- execution/actuation deserves a separate formal layer

Not borrowed:

- old topic identity
- old payload layout
- old compatibility requirements

## Scope boundary

Current v1 only freezes:

- bundle identity
- surface kind
- small atom vocabulary
- per-atom timing and payload slots

Current v1 does not freeze:

- device-specific injection protocols
- adapter lines
- feedback channels
- game-specific gear-control semantics
- full touch gesture grammar

Those remain future work.

## Why this line matters

Without a separate actuation layer, the repository would drift into mixing:

- interaction semantics
- execution bundle semantics
- lifecycle/reporting semantics

That would recreate the exact ambiguity this repository was created to avoid.

## Future refinement directions

Later refinements may add:

- richer device-specific atom payloads
- injection and adapter-side schemas
- feedback bundle or execution receipt line
- more precise time bases
- expanded touch/gamepad/gear-control vocabularies

The first step is only to create a clean formal actuation bundle line.
