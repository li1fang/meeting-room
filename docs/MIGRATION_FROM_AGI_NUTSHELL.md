# Migration From AGI-Nutshell

This repository replaces AGI-Nutshell as the main working contract repository for the Natural Control formal line.

## Migration position

- AGI-Nutshell remains a reference and legacy-inventory source.
- `meeting-room` is now the active NC-first contract repository.
- Migration is semantic, not compatibility-driven.

## What moved directly

The following content moved directly as the new baseline:

- `naturalcontrol.common.v1.2`
- `naturalcontrol.interaction_request.v1.2`
- `naturalcontrol.interaction_frame.v1.2`
- `naturalcontrol.interaction_trace_pack.v1.2`
- minimal samples
- terminology
- formal schema note

## What was borrowed but rewritten

Borrowed from AGI-Nutshell in form only:

- registry / genesis pattern
- TCK runner and suite layout
- governance and schema note layering

Rewritten here:

- naming rules
- envelope rules
- canonical tree rules
- NC-first documentation
- linting and topic consistency rules

## What was not migrated

Not migrated as the NC formal line:

- `naturalcontrol.requests.v3`
- `naturalcontrol.atoms.v3`
- old universal event envelope
- mirror-tree layout (`domains/**`)
- weak SARF zone model

## Legacy mapping

### Legacy automation assets

- old `tap/swipe/text/key` semantics stay legacy
- they are not treated as Natural Control formal semantics

### Lifecycle/reporting candidates

- `ack/progress/result` may later return as a reporting/orchestration layer
- they are not part of the current `request/frame/trace` baseline

### Actuation candidate

- `nc.control.bundle.v1` remains a future actuation/execution reference

### Estimation reference

- richer NP frame/body semantics remain future estimation references

## Current migration rule

Do not attempt compatibility-first migration.
Move only what strengthens the new formal baseline.
