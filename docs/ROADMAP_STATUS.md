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

The interaction baseline and lifecycle/reporting semantics are formally separated in the repository.

### #5 estimation v1.1 line

Status: landed as current recommended draft

What now exists:

- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`
- `naturalcontrol.estimation_observation.v1.1`
- `naturalcontrol.estimation_prediction.v1.1`
- minimal samples
- minimal TCK suites
- formal design note for `v1.1`

Interpretation:

The repository now has a richer recommended estimation line while preserving the original `v1` skeleton as seed/reference.

### #6 body keypoint catalog

Status: landed as document-level canonical catalog

What now exists:

- `docs/NC-BODY-KEYPOINT-CATALOG-v1.md`
- terminology aligned to the initial canonical keypoint set

Interpretation:

The repository now has a small canonical naming surface for body-keypoint usage inside estimation drafts.

### #7 actuation v1.1 + receipt line

Status: landed as current recommended draft

What now exists:

- `naturalcontrol.actuation_bundle.v1`
- `naturalcontrol.actuation_bundle.v1.1`
- `naturalcontrol.actuation_receipt.v1`
- minimal samples
- minimal TCK suites
- formal design note for `v1.1`

Interpretation:

The repository now has a richer recommended actuation bundle line plus the first actuation-side receipt line, while preserving the original `v1` bundle skeleton as seed/reference.

### Reserved domain expansion path

Status: unchanged and still landed as repository rule

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
3. NC estimation line (`v1.1` recommended, `v1` retained as skeleton seed)
4. NC actuation line (`v1.1` recommended, `v1` retained as skeleton seed)
5. reserved multi-domain expansion path

## Current recommendation

Do not widen scope to 3D, ballistic, or active non-NC domain schemas before the following are stable:

- interaction baseline examples
- lifecycle/reporting semantics
- estimation v1.1 terminology and body-keypoint catalog
- actuation v1.1 bundle/receipt semantics
- reserved-domain governance rules
