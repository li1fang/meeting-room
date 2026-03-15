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
- `naturalcontrol.estimation_observation.v1.2`
- `naturalcontrol.actuation_adapter_receipt.v1`

Stable lines may later use major-only naming if needed, but that is not the only allowed form here.

## Envelope lines

The current NC formal lines use native payload identity:

- `schema_id`
- `spec_version`
- `epoch_ns`

Legacy event-envelope fields such as `schema/event_id/event_ts/producer` are not universal requirements in this repository.

## Current NC interaction baseline

Canonical schema files:

- `schemas/nc/naturalcontrol.common.v1.2.schema.json`
- `schemas/nc/naturalcontrol.interaction_request.v1.2.schema.json`
- `schemas/nc/naturalcontrol.interaction_frame.v1.2.schema.json`
- `schemas/nc/naturalcontrol.interaction_trace_pack.v1.2.schema.json`

Canonical sample files:

- `samples/naturalcontrol.interaction_request.v1.2/minimal.json`
- `samples/naturalcontrol.interaction_frame.v1.2/minimal.json`
- `samples/naturalcontrol.interaction_trace_pack.v1.2/minimal.json`

## Current lifecycle/reporting line

Canonical schema files:

- `schemas/nc/naturalcontrol.lifecycle_ack.v1.schema.json`
- `schemas/nc/naturalcontrol.lifecycle_progress.v1.schema.json`
- `schemas/nc/naturalcontrol.lifecycle_result.v1.schema.json`

Canonical sample files:

- `samples/naturalcontrol.lifecycle_ack.v1/minimal.json`
- `samples/naturalcontrol.lifecycle_progress.v1/minimal.json`
- `samples/naturalcontrol.lifecycle_result.v1/minimal.json`

## Estimation line

Seed skeleton schema files:

- `schemas/nc/naturalcontrol.estimation_observation.v1.schema.json`
- `schemas/nc/naturalcontrol.estimation_prediction.v1.schema.json`

Recommended draft schema files:

- `schemas/nc/naturalcontrol.estimation_observation.v1.2.schema.json`
- `schemas/nc/naturalcontrol.estimation_prediction.v1.2.schema.json`

Reference draft schema files retained:

- `schemas/nc/naturalcontrol.estimation_observation.v1.1.schema.json`
- `schemas/nc/naturalcontrol.estimation_prediction.v1.1.schema.json`

Canonical sample files for the recommended line:

- `samples/naturalcontrol.estimation_observation.v1.2/minimal.json`
- `samples/naturalcontrol.estimation_prediction.v1.2/minimal.json`

## Actuation line

Seed skeleton schema file:

- `schemas/nc/naturalcontrol.actuation_bundle.v1.schema.json`

Recommended draft schema files:

- `schemas/nc/naturalcontrol.actuation_bundle.v1.1.schema.json`
- `schemas/nc/naturalcontrol.actuation_adapter_receipt.v1.schema.json`
- `schemas/nc/naturalcontrol.actuation_injector_receipt.v1.schema.json`
- `schemas/nc/naturalcontrol.actuation_device_receipt.v1.schema.json`

Reference receipt schema retained:

- `schemas/nc/naturalcontrol.actuation_receipt.v1.schema.json`

Canonical sample files for the recommended line:

- `samples/naturalcontrol.actuation_bundle.v1.1/minimal.json`
- `samples/naturalcontrol.actuation_adapter_receipt.v1/minimal.json`
- `samples/naturalcontrol.actuation_injector_receipt.v1/minimal.json`
- `samples/naturalcontrol.actuation_device_receipt.v1/minimal.json`
