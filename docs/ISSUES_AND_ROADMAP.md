# Issues and Roadmap (v1)

## Current repository issues

### 1. Formal line is still 2D-only

Current `v1.2` intentionally stops at the 2D interaction baseline.
We still need later formal lines for:

- estimation
- actuation
- 3D / ballistic systems

### 2. NC lifecycle contracts are not yet rebuilt here

The repository currently carries `request/frame/trace` only.
Later we may add an NC reporting/orchestration layer, but not before the current baseline is stable.

### 3. NP / PS / TS extension slots are reserved but empty

This is intentional for v1.
The repository is NC-first, not multi-domain-complete yet.

### 4. No compatibility layer for legacy AGI-Nutshell

This is an explicit choice.
It keeps the repository clean, but means migration adapters may be needed later at the implementation edge.

## Roadmap

### Phase 1 — Stabilize NC formal baseline

- keep `v1.2` coherent
- refine terminology
- refine request/frame/trace examples
- align consumers to the new line

### Phase 2 — Add NC lifecycle/reporting line

Possible future line:

- ack / progress / result replacement or successor
- execution/reporting semantics separated from interaction semantics

### Phase 3 — Add estimation layer

Future work may formalize:

- predicted target state
- richer kinematics
- body-part semantics
- confidence / uncertainty

### Phase 4 — Add actuation layer

Future work may formalize:

- execution bundles
- device control surfaces
- mapping from interaction layer to execution layer

### Phase 5 — Revisit multi-domain expansion

Only after NC baseline is stable:

- NP formal integration surface
- PS formal integration surface
- TS formal integration surface
