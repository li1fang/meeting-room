# AGI-Nutshell Legacy Inventory

This document records what was borrowed from AGI-Nutshell and what was intentionally not carried into this repository.

## Borrowed

### Governance / structure ideas

- registry-driven topic bookkeeping
- TCK runner + suite structure
- governance and schema notes as first-class docs
- retention / throughput / partition-key awareness

### Possible future candidates

- `nc.control.bundle.v1`
  - useful as an actuation / execution bundle reference
  - not suitable as request semantics
- `np.perception.frame.v1`
  - useful as a future estimation / richer target-state reference
  - not part of current NC v1.2 baseline

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
- not appropriate as the universal base for the NC formal line

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
- may still be useful later as orchestration or reporting contracts

### Actuation candidate

- `nc.control.bundle.v1`

Current value:
- useful reference for future execution/actuation layer
- intentionally excluded from current request/frame/trace baseline

### Estimation reference

- `np.perception.frame.v1`

Current value:
- useful reference for future richer target-state or 3D estimation work
- intentionally excluded from current NC-first repository baseline
