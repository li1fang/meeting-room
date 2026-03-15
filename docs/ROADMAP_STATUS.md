# Roadmap Status

Current mainline view of the first formal work tracked in GitHub issues.

## Current status

### #1 lifecycle/reporting line

Status: in progress, first landing complete in-repo

What now exists:

- `naturalcontrol.lifecycle_ack.v1`
- `naturalcontrol.lifecycle_progress.v1`
- `naturalcontrol.lifecycle_result.v1`
- minimal samples
- minimal TCK suites
- formal design note

Interpretation:

The interaction baseline and the lifecycle/reporting line are now separated in the repository.
The lifecycle line is still young, but it is no longer only a placeholder issue.

### #2 estimation layer

Status: open, not landed

Current repository stance:

- reserved for future work
- not part of the current 2D baseline
- not yet represented by schema files in this repository

### #3 actuation layer

Status: open, not landed

Current repository stance:

- reserved for future work
- execution/actuation semantics remain separate from the current interaction baseline

### #4 NP/PS/TS reserved expansion path

Status: open, not landed

Current repository stance:

- repository remains NC-first
- future non-NC domains are still reserved slots, not active schema lines

## Mainline view

The current mainline of `meeting-room` is now:

1. NC interaction baseline (`request/frame/trace`)
2. NC lifecycle/reporting line (`ack/progress/result` successor)
3. deferred estimation layer
4. deferred actuation layer
5. deferred multi-domain expansion

## Current recommendation

Do not widen scope before the following are stable:

- the interaction baseline examples
- the lifecycle/reporting line semantics
- the terminology shared between both lines
