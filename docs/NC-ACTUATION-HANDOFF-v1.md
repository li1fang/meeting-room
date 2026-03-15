# NC Actuation Handoff v1

Status: Draft

## Purpose

This document defines the handoff line that sits between the current actuation bundle and the already-split execution receipts.

It adds two explicit contract units:

- `naturalcontrol.actuation_adapter_bundle.v1`
- `naturalcontrol.actuation_injector_batch.v1`

The goal is to freeze what adapter and injector actually hand to each other before the repository goes any deeper into backend-specific protocol work.

## Why this line exists

The repository already has:

- `naturalcontrol.actuation_bundle.v1.1`
- `naturalcontrol.actuation_adapter_receipt.v1`
- `naturalcontrol.actuation_injector_receipt.v1`
- `naturalcontrol.actuation_device_receipt.v1`

That is enough to describe ownership and receipts, but it still leaves one production-critical gap:

- what adapter hands to injector
- what injector prepares as its own emission batch

This handoff line closes that gap without freezing OS-specific packet grammar.

## Handoff chain

The current actuation chain is now:

1. `naturalcontrol.actuation_bundle.v1.1`
2. `naturalcontrol.actuation_adapter_bundle.v1`
3. `naturalcontrol.actuation_injector_batch.v1`
4. `naturalcontrol.actuation_adapter_receipt.v1`
5. `naturalcontrol.actuation_injector_receipt.v1`
6. `naturalcontrol.actuation_device_receipt.v1`

Interpretation:

- `bundle` = surface-level execution intent
- `adapter_bundle` = adapter-owned translated bundle
- `injector_batch` = injector-owned emission batch
- receipts remain receipts only

## `naturalcontrol.actuation_adapter_bundle.v1`

Use this topic when an adapter has accepted a `naturalcontrol.actuation_bundle.v1.1` payload and translated it into an adapter-owned handoff unit.

It is for:

- translated execution items
- adapter ownership and traceability
- stable handoff to injector

It is not for:

- backend packet details
- device-native event logs
- receipt semantics

## `naturalcontrol.actuation_injector_batch.v1`

Use this topic when an injector/backend has accepted an adapter bundle and prepared an injector-owned emission batch.

It is for:

- injector ownership and backend selection
- emission-ready operation grouping
- stable handoff to the execution edge

It is not for:

- OS/driver-native event schemas
- device-observed feedback
- receipt semantics

## Scope boundary

Current v1 freezes:

- adapter-owned translated bundle shape
- injector-owned emission batch shape
- link fields between bundle, handoff, batch, and receipt lines
- channel and kind vocabularies at the contract level

Current v1 does not freeze:

- adapter-specific protocol schemas
- injector packet binary grammar
- driver-level native event schemas
- device-native feedback/event lines

## Pause-point intent

This line is intentionally the nearest pause point for the repository.

Once these two topics are landed, the repository has enough structure to support real adapter/injector implementation work without forcing premature backend-specific contract expansion.
