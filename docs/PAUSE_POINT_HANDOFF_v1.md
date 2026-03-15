# Pause Point: Handoff v1

Status: Current pause point

## What is now considered stable enough

The repository has now landed:

- interaction baseline `v1.2`
- lifecycle/reporting line `v1`
- estimation line with `v1.2` as the current recommended draft
- actuation bundle line with `v1.1` as the current recommended bundle draft
- explicit handoff line:
  - `naturalcontrol.actuation_adapter_bundle.v1`
  - `naturalcontrol.actuation_injector_batch.v1`
- split execution receipts:
  - `naturalcontrol.actuation_adapter_receipt.v1`
  - `naturalcontrol.actuation_injector_receipt.v1`
  - `naturalcontrol.actuation_device_receipt.v1`

This is enough to stop and let production implementations catch up.

## What is explicitly deferred

Deferred until real production pull exists:

- adapter-specific protocol schemas
- injector packet grammar
- device-native feedback/event schemas
- ballistic schemas
- 3D world-space standards
- active NP / PS / TS schema lines

## Restart conditions

Resume contract expansion only when at least one of these becomes true:

- a real adapter or injector implementation needs contract support that the current handoff line cannot express
- cross-team integration exposes a missing minimum semantic in the handoff or receipt chain
- estimation work needs a new contract line for actual production usage rather than exploratory vocabulary

## Repository stance at this pause point

The repository remains NC-first.
It is paused after landing a useful handoff layer, not because the design is complete, but because the next steps would otherwise force premature protocol detail.
