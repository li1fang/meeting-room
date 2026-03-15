# GOVERNANCE

## Repository stance

This repository is NC-first.
It is designed to freeze the Natural Control formal line before broader multi-domain expansion.

## Naming and versioning

- Direct minor-version naming is allowed.
- Formal draft lines may use names such as `*.v1.2` directly.
- Breaking changes still require a new topic name.
- Stable and draft lines may coexist.

## Canonical rules

- Root tree is the only canonical tree.
- Every registered topic must have:
  - one schema file
  - one minimal sample
  - one TCK suite
- No mirror trees.

## Current mandatory identity for NC formal line

Current NC formal draft payloads must carry:

- `schema_id`
- `spec_version`
- `epoch_ns`

They may additionally carry request/trace/frame-specific identifiers, but they do not inherit a universal legacy event envelope.

## Draft vs stable

Current `v1.2` line is a formal draft, not yet a final frozen universal contract.
It is stable enough for review and implementation alignment, but not treated as permanent final form across all future domains.

## Current repository quality gate

A topic is not considered landed unless all of the following exist and pass:

- schema JSON parses
- minimal sample validates against schema
- TCK suite passes
- registry entry exists
- docs are consistent with the actual schema line


## Current lifecycle/reporting line

The repository now carries a separate lifecycle/reporting line:

- `naturalcontrol.lifecycle_ack.v1`
- `naturalcontrol.lifecycle_progress.v1`
- `naturalcontrol.lifecycle_result.v1`

These topics are separate from the interaction baseline and must not be used to redefine request/frame/trace semantics.
