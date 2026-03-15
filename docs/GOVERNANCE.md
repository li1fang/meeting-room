# GOVERNANCE

## Repository stance

This repository is NC-first.
It freezes the Natural Control formal lines before broader multi-domain expansion.

## Naming and versioning

- Direct minor-version naming is allowed.
- Formal draft lines may use names such as `*.v1.2` or `*.v1.1` directly.
- Breaking changes still require a new topic name.
- Stable and draft lines may coexist.

## Canonical rules

- Root tree is the only canonical tree.
- Every registered topic must have:
  - one schema file
  - one minimal sample
  - one TCK suite
- No mirror trees.

## Current mandatory identity for NC formal lines

Current NC formal payloads must carry:

- `schema_id`
- `spec_version`
- `epoch_ns`

They may additionally carry line-specific identifiers, but they do not inherit a universal legacy event envelope.

## Draft vs stable

Current `v1.2` interaction line is a formal draft, not yet a final frozen universal contract.
The lifecycle, estimation, and actuation lines are also draft lines.
All are stable enough for review and implementation alignment, but none are yet treated as permanent final form across all future domains.

## Seed skeleton vs richer draft

When a seed skeleton line already exists, the repository does **not** mutate that line in place to become a richer draft.
Instead:

- keep the seed topic as landed reference
- add a new topic name for the richer draft line
- update docs and registry to mark which line is currently recommended

That is why this repository keeps:

- `naturalcontrol.estimation_observation.v1` and `naturalcontrol.estimation_prediction.v1` as skeleton seeds
- `naturalcontrol.estimation_observation.v1.1` and `naturalcontrol.estimation_prediction.v1.1` as retained reference drafts
- `naturalcontrol.estimation_observation.v1.2` and `naturalcontrol.estimation_prediction.v1.2` as the current recommended draft estimation line
- `naturalcontrol.actuation_bundle.v1` as a skeleton seed
- `naturalcontrol.actuation_bundle.v1.1` as the current recommended bundle line
- `naturalcontrol.actuation_adapter_bundle.v1` and `naturalcontrol.actuation_injector_batch.v1` as the current recommended handoff line
- `naturalcontrol.actuation_receipt.v1` as a broad retained receipt seed
- `naturalcontrol.actuation_adapter_receipt.v1`, `naturalcontrol.actuation_injector_receipt.v1`, and `naturalcontrol.actuation_device_receipt.v1` as the current recommended execution-receipt line

## Current repository quality gate

A topic is not considered landed unless all of the following exist and pass:

- schema JSON parses
- minimal sample validates against schema
- TCK suite passes
- registry entry exists
- docs are consistent with the actual schema line

## Current landed NC lines

The repository now carries these separate NC lines:

- interaction baseline
- lifecycle/reporting line
- estimation line
- actuation line

These lines must stay separated.
No line may redefine another line's ownership just to avoid creating a new schema.

## Future domain expansion rule

Future non-NC domains may land here later, but only under these conditions:

- they use the same root canonical tree
- they bring a boundary document
- they bring a real schema, sample, and TCK
- they update registry and repository docs together

Reserved domains do not justify fake placeholder topics.
