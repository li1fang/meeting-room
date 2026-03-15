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

Status: landed as retained reference draft

What now exists:

- `naturalcontrol.estimation_observation.v1`
- `naturalcontrol.estimation_prediction.v1`
- `naturalcontrol.estimation_observation.v1.1`
- `naturalcontrol.estimation_prediction.v1.1`

Interpretation:

The repository preserves the first richer estimation draft line as reference instead of mutating it in place.

### #6 body keypoint catalog

Status: landed as document-level canonical catalog

What now exists:

- `docs/NC-BODY-KEYPOINT-CATALOG-v1.md`
- terminology aligned to the initial canonical keypoint set

Interpretation:

The repository has a small canonical naming surface for body-keypoint usage inside estimation drafts.

### #7 actuation v1.1 + receipt line

Status: landed as retained bundle draft plus broad receipt seed

What now exists:

- `naturalcontrol.actuation_bundle.v1`
- `naturalcontrol.actuation_bundle.v1.1`
- `naturalcontrol.actuation_receipt.v1`

Interpretation:

The repository preserves the first richer actuation bundle line and the broad receipt seed instead of mutating them in place.

### #8 estimation v1.2 line

Status: landed as current recommended draft

What now exists:

- `naturalcontrol.estimation_observation.v1.2`
- `naturalcontrol.estimation_prediction.v1.2`
- minimal samples
- minimal TCK suites
- formal design note for `v1.2`

Interpretation:

The repository now has a tighter recommended estimation line that freezes structured uncertainty and optional 3D expression without reopening the 3D / ballistic mainline.

### #9 uncertainty + optional 3D formalization

Status: landed inside estimation `v1.2`

What now exists:

- uncertainty models with explicit 2D/3D region shapes
- confidence-level field in prediction uncertainty
- self-contained optional 3D geometry and kinematics objects

Interpretation:

The repository can now express richer prediction confidence and optional 3D state in a controlled way instead of leaving those payloads loose.

### #10 actuation execution receipt split

Status: landed as current recommended execution-receipt line

What now exists:

- `naturalcontrol.actuation_adapter_receipt.v1`
- `naturalcontrol.actuation_injector_receipt.v1`
- `naturalcontrol.actuation_device_receipt.v1`
- minimal samples
- minimal TCK suites
- execution receipt design note

Interpretation:

The repository now separates adapter, injector, and device-facing execution receipts instead of collapsing all execution ownership into one generic receipt.

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
3. NC estimation line (`v1.2` recommended, `v1.1` retained as reference, `v1` retained as skeleton seed)
4. NC actuation line (`v1.1` bundle recommended, split execution receipts recommended, `v1` retained as skeleton seed)
5. reserved multi-domain expansion path

## Current recommendation

Do not widen scope to 3D, ballistic, or active non-NC domain schemas before the following are stable:

- interaction baseline examples
- lifecycle/reporting semantics
- estimation v1.2 uncertainty and optional 3D semantics
- actuation execution receipt ownership boundaries
- reserved-domain governance rules
