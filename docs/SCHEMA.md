# SCHEMA

All schemas in this repository use JSON Schema draft 2020-12.

## Canonical placement

Only the root canonical tree is valid:

- `schemas/**`
- `samples/**`
- `tck/**`
- `docs/**`

There is no mirrored `domains/**` tree in this repository.

## Naming

This repository allows direct minor-version schema naming for formal draft lines.
Examples:

- `naturalcontrol.interaction_request.v1.2`
- `naturalcontrol.interaction_frame.v1.2`
- `naturalcontrol.interaction_trace_pack.v1.2`

Stable lines may later use major-only naming if needed, but that is not the only allowed form here.

## Envelope lines

The current NC formal line uses native payload identity:

- `schema_id`
- `spec_version`
- `epoch_ns`

Legacy event-envelope fields such as `schema/event_id/event_ts/producer` are not universal requirements in this repository.

## Current NC formal line

Canonical schema files:

- `schemas/nc/naturalcontrol.common.v1.2.schema.json`
- `schemas/nc/naturalcontrol.interaction_request.v1.2.schema.json`
- `schemas/nc/naturalcontrol.interaction_frame.v1.2.schema.json`
- `schemas/nc/naturalcontrol.interaction_trace_pack.v1.2.schema.json`

Canonical sample files:

- `samples/naturalcontrol.interaction_request.v1.2/minimal.json`
- `samples/naturalcontrol.interaction_frame.v1.2/minimal.json`
- `samples/naturalcontrol.interaction_trace_pack.v1.2/minimal.json`
