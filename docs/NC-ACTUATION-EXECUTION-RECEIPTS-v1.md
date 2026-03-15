# NC Actuation Execution Receipts v1

Status: Draft

## Purpose

This document defines the next actuation layer step for `meeting-room`.
It splits the broad `naturalcontrol.actuation_receipt.v1` concept into three more explicit execution-side receipt lines:

- adapter receipt
- injector receipt
- device receipt

The generic `naturalcontrol.actuation_receipt.v1` line remains in the repository unchanged.
It stays as the broad receipt seed/reference.

## Why this split exists

`actuation_receipt.v1` is useful, but too broad to express execution ownership cleanly.
The next step is to separate where a bundle is:

- accepted or translated by an adapter
- injected by an injector/backend
- observed or confirmed at the device-facing edge

This avoids collapsing all execution-side feedback into one generic receipt.

## New lines

This repository adds:

- `naturalcontrol.actuation_adapter_receipt.v1`
- `naturalcontrol.actuation_injector_receipt.v1`
- `naturalcontrol.actuation_device_receipt.v1`

These lines are siblings to `naturalcontrol.actuation_receipt.v1`.
They do not replace lifecycle/reporting.

## Ownership boundary

### Adapter receipt

Adapter receipt is for:

- bundle acceptance by an adapter
- translation or shaping readiness
- handoff to a downstream injector

It is not for:

- low-level injection outcome
- device observation

### Injector receipt

Injector receipt is for:

- injector/backend acceptance
- packet or command injection result
- handoff toward the device-facing surface

It is not for:

- adapter-side translation state
- device-observed confirmation

### Device receipt

Device receipt is for:

- device-facing observation or confirmation
- low-level readback or observed event counts
- the closest contract-level receipt to the execution edge

It is not for:

- adapter acceptance
- injector translation or batching decisions

## Scope boundary

Current v1 freezes:

- ownership split between adapter / injector / device receipts
- minimal receipt-state vocabulary for each line
- identifiers that connect receipts back to bundle and execution

Current v1 still does not freeze:

- adapter-specific protocol contracts
- injector-specific packet schemas
- driver-level or OS-level event schemas
- device-native feedback grammars

## Borrowing stance from AGI-Nutshell

This line borrows only the layering instinct that execution feedback should not be one undifferentiated channel.
It does not borrow old topic naming, old envelope shape, or old compatibility requirements.
