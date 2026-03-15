# AGI-Nutshell Legacy Inventory

This document records what was borrowed from AGI-Nutshell and what was intentionally not carried into this repository.

## Borrowed

### Governance / structure ideas

- registry-driven topic bookkeeping
- TCK runner + suite structure
- governance and schema notes as first-class docs
- retention / throughput / partition-key awareness

### Borrowed into current landed lines

- lifecycle/reporting line
  - borrowed the idea that admission, in-flight progress, and terminal state deserve a separate line
  - not borrowed as old topic names or old envelopes
- estimation line
  - borrowed the idea that richer subject-state expression belongs in its own layer
  - not borrowed as old perception topic shapes or old compatibility rules
- actuation line
  - borrowed the idea that execution bundles belong in their own layer
  - not borrowed as `nc.control.bundle.v1` compatibility
- estimation v1.1
  - borrowed the richer-state-expression direction from older perception work
  - not borrowed as old wire identity, old envelope, or old payload layout
- actuation v1.1
  - borrowed the execution-bundle layering direction from older actuation-oriented work
  - not borrowed as old topic naming or execution-wire compatibility

### Possible future candidates

- `np.perception.frame.v1`
  - useful as a future estimation / richer target-state reference
  - not part of current NC baseline

## Explicitly rejected from the NC formal line

### Legacy automation semantics

- `naturalcontrol.requests.v3`
- `naturalcontrol.atoms.v3`

Reason:

- these model `tap/swipe/text/key` style automation
- they do not model Natural Control request / frame / trace semantics

### Old universal envelope

- `schema`
- `event_id`
- `event_ts`
- `producer`

Reason:

- acceptable for old event topics
- not appropriate as the universal base for the NC formal lines

### Mirror trees

- `domains/**` + `schemas/**` dual-tree layout

Reason:

- duplicates drift
- canonical placement becomes ambiguous

### Weak SARF zone shape

Reason:

- too weak for target/safe/reversible/forbidden policy modeling
- insufficient for NC intelligent-miss contract design

## Classification of legacy NC assets

### Legacy automation assets

- `naturalcontrol.requests.v3`
- `naturalcontrol.atoms.v3`

Current value:

- not part of current Natural Control formal line
- may only be useful later if a separate mobile / touch automation line is split out

### Lifecycle / reporting candidates

- `naturalcontrol.ack.v3`
- `naturalcontrol.progress.v3`
- `naturalcontrol.result.v3`

Current value:

- not interaction semantics
- useful only as historical motivation for a separate lifecycle/reporting line

### Actuation candidate

- `nc.control.bundle.v1`

Current value:

- useful reference for execution/actuation layering
- intentionally not used as a compatibility target

### Estimation reference

- `np.perception.frame.v1`

Current value:

- useful reference for richer target-state or 3D estimation work
- intentionally excluded from the current NC-first repository baseline
