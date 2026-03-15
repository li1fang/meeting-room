# Roadmap Status

Current mainline view of the formal work tracked in GitHub issues.

## Current status

### #1 lifecycle/reporting line

Status: landed

What now exists:

- `naturalcontrol.lifecycle_ack.v1`
- `naturalcontrol.lifecycle_progress.v1`
- `naturalcontrol.lifecycle_result.v1`
- minimal samples
- minimal TCK suites
- formal design note

Interpretation:

The interaction baseline and lifecycle/reporting semantics are now formally separated in the repository.

### #2 estimation layer

Status: landed as draft skeleton

What now exists:

- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`
- minimal samples
- minimal TCK suites
- formal design note

Interpretation:

The repository now has a formal place for observation and prediction semantics without forcing those concerns into interaction or actuation payloads.

### #3 actuation layer

Status: landed as draft skeleton

What now exists:

- `naturalcontrol.actuation_bundle.v1`
- minimal sample
- minimal TCK suite
- formal design note

Interpretation:

Execution-bundle semantics now have a formal home that stays separate from both interaction and lifecycle lines.

### #4 NP/PS/TS reserved expansion path

Status: landed as repository rule

What now exists:

- canonical placement rule for future domains
- minimum landing requirements for non-NC domains
- explicit reserved-path document

Interpretation:

The repository stays NC-first while making future NP/PS/TS growth explicit and disciplined.

## Mainline view

The current mainline of `meeting-room` is now:

1. NC interaction baseline (`request/frame/trace`)
2. NC lifecycle/reporting line
3. NC estimation line (draft skeleton)
4. NC actuation line (draft skeleton)
5. reserved multi-domain expansion path

## Current recommendation

Do not widen scope to 3D, ballistic, or active non-NC domain schemas before the following are stable:

- interaction baseline examples
- lifecycle/reporting semantics
- estimation and actuation terminology
- reserved-domain governance rules
