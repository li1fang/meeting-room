# NC Actuation Layer v1.1

Status: Draft

## Purpose

This document defines the next actuation draft line for `meeting-room`.
It deepens the existing `v1` bundle skeleton and adds the first actuation-side receipt line.

The actuation layer continues to own:

- execution bundles
- device-facing atoms
- bundle-to-surface shaping
- actuation-side receipt state

It still does not own:

- action-target intent planning
- estimation or prediction state
- lifecycle admission/progress/result semantics

## Versioning position

The repository now carries two actuation levels:

- `naturalcontrol.actuation_bundle.v1`

This remains the first skeleton seed.

The current recommended actuation draft line becomes:

- `naturalcontrol.actuation_bundle.v1.1`
- `naturalcontrol.actuation_receipt.v1`

This repository intentionally uses a new topic name for the richer bundle line instead of mutating `v1` in place.

## New semantics in v1.1

Compared with the v1 skeleton, v1.1 adds:

- required `surface_profile_ref`
- explicit `channel` per atom
- richer touch / stick / gear payload shapes
- optional `adapter_ref`
- first receipt line for actuation-side feedback

## Payload roles

### `naturalcontrol.actuation_bundle.v1.1`

Use for a device-facing bundle of execution atoms.

Required top-level fields:

- `schema_id`
- `spec_version`
- `epoch_ns`
- `bundle_id`
- `request_id`
- `interaction_id`
- `execution_id`
- `surface_kind`
- `time_basis`
- `surface_profile_ref`
- `atoms[]`

Each atom carries:

- `atom_id`
- `offset_ns`
- `duration_ns`
- `kind`
- `channel`
- `payload`

### `naturalcontrol.actuation_receipt.v1`

Use for actuation-side acceptance or emission reporting.

Required top-level fields:

- `schema_id`
- `spec_version`
- `epoch_ns`
- `receipt_id`
- `bundle_id`
- `execution_id`
- `surface_kind`
- `receipt_state`

This line does not replace lifecycle/reporting.
It only reports bundle-side receipt facts.

## Relationship to older execution bundles

This line borrows only the layering idea from older execution-bundle work such as `nc.control.bundle.v1`.
It does not adopt that topic name, payload shape, or compatibility policy.

Borrowed idea:

- execution/actuation deserves a separate formal layer

Not borrowed:

- old topic identity
- old payload layout
- old compatibility requirements

## Scope boundary

Current v1.1 freezes:

- bundle identity
- surface profile reference
- per-atom channel and payload shape
- first receipt-state line

Current v1.1 still does not freeze:

- injector-specific schemas
- adapter-specific protocol schemas
- deep touch gesture grammar
- game-specific gear semantics
- low-level device driver contracts

## Why this line matters

Without a richer actuation line, the repository would either keep execution semantics too weak to be useful or leak device-facing concerns back into interaction and lifecycle lines.

v1.1 avoids both outcomes while preserving the v1 seed.
