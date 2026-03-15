# NaturalControl Formal Terminology / 自然控制正式术语表

Status: Draft

This glossary explains how NC uses core terms in contracts, runtime traces, and debugging.

本术语表用于解释 NC 在正式契约、运行时轨迹和调试资料中的核心术语，不是逐词翻译表。

## Principles / 原则

- One concept should ideally keep one stable name.
- Prefer common engineering words over custom metaphors.
- External contract words and internal algorithm words should stay separate.

- 一个概念最好只保留一个稳定名字。
- 优先使用常见工程词，而不是内部隐喻词。
- 对外契约词汇和对内算法词汇应分开使用。

## Terms / 术语

### `action target` / `动作目标`

What it means:
- The smallest external instruction unit sent into NC.
- It says where an event may or should happen.
- The only required geometry is a `bbox`.

解释：
- 这是外部传给 NC 的最小动作单元。
- 它表达“某个事件应该或允许在什么区域发生”。
- 唯一必须提供的几何信息是 `bbox`。

What it is not:
- Not a full trajectory.
- Not a final exact click point.

不是：
- 不是整条轨迹。
- 不是最终精确落点。

### `event` / `事件`

What it means:
- A discrete action on the timeline, such as `press`, `release`, `pause_start`, `pause_end`.

解释：
- 时间轴上的离散动作，例如 `press`、`release`、`pause_start`、`pause_end`。

### `cluster` / `事件簇`

What it means:
- A runtime-confirmed group of related events and related motion.
- A cluster ends only after the event group has completed and motion has naturally settled.

解释：
- 运行时确认出来的一组相关事件及其相关运动。
- 只有当这一组事件已完成，并且运动自然停稳后，cluster 才结束。

Why this word:
- It is easier to explain than custom internal terms such as "control atom".

为什么用这个词：
- 比“控制原子”这类内部词更容易对外解释。

### `cluster hint` / `事件簇提示`

What it means:
- An external hint about which action targets may belong together.
- It is advisory only.
- NC confirms the final `cluster_id`.

解释：
- 外部给出的提示，表示哪些动作目标可能属于同一簇。
- 它只是提示，不是最终裁决。
- 最终 `cluster_id` 由 NC 输出侧确认。

### `natural settle` / `自然停稳`

What it means:
- Motion has slowed and paused enough to count as the end of a cluster.
- It is not just "velocity equals zero".

解释：
- 轨迹已经减速并停顿到足以视作 cluster 结束的程度。
- 它不等于数学上的“速度等于 0”。

### `zone map` / `区域图`

What it means:
- A structured set of screen regions that constrain or shape NC behavior.
- Zones describe what is intended, safe, reversible, or forbidden.

解释：
- 一组结构化的屏幕区域，用来约束或塑造 NC 行为。
- 它描述哪些区域是目标、安全误点、可回退误点、或绝对禁入。

### `zone map availability` / `区域图可用性`

What it means:
- Whether a payload carries a real zone list, an explicit unknown envelope, or a deliberate not-provided envelope.
- This exists to keep trace packs audit-complete without inventing fake zones.

解释：
- 表示当前 payload 中的区域图，究竟是有真实区域列表、显式未知，还是明确未提供。
- 这个概念存在的目的，是让 trace pack 在审计上完整，而不必伪造假的 zone。

### `target zone` / `目标区`

What it means:
- A zone meant for successful task completion.

解释：
- 用于完成任务命中的区域。

### `safe miss zone` / `安全误点区`

What it means:
- A zone where NC may miss without meaningful consequence.

解释：
- NC 可以误点而不会产生明显后果的区域。

### `reversible miss zone` / `可回退误点区`

What it means:
- A zone where a miss is allowed because a known rollback path exists.

解释：
- 允许误点，但系统已知如何回退的区域。

### `forbidden zone` / `禁入区`

What it means:
- A zone that must never be entered by error policy or exploration.

解释：
- 在错误策略或探索行为中都绝对不能进入的区域。

### `rollback action` / `回退动作`

What it means:
- A structured recovery step, such as a key chord, mouse button, system back, pointer gesture, or wait.

解释：
- 一种结构化恢复动作，例如组合键、鼠标按钮、系统返回、指针手势或等待。

### `kinematics` / `运动学信息`

What it means:
- Motion facts such as velocity, acceleration, and confidence.
- This is how dynamic pursuit becomes explicit in the contract.

解释：
- 速度、加速度、置信度等运动事实。
- 动态追击能力需要通过这类字段显式进入契约。

### `coordinate space` / `坐标空间`

What it means:
- The declared geometry space used by the contract.
- Example values: `screen_px`, `viewport_px`, `normalized_0_1`.

解释：
- 契约所声明使用的几何坐标空间。
- 例如：`screen_px`、`viewport_px`、`normalized_0_1`。

### `interaction request` / `交互请求`

What it means:
- The external input contract sent into NC.
- It contains intent-side information, not NC's final output trajectory.

解释：
- 外部传给 NC 的输入契约。
- 它承载的是意图侧信息，而不是 NC 的最终输出轨迹。

### `interaction frame` / `交互帧`

What it means:
- A streaming alignment unit.
- It carries current cursor state, target snapshots, timing facts, and current zone state.

解释：
- 用于在线对齐的流式单元。
- 它携带当前光标状态、目标快照、时间事实和当前区域状态。

### `interaction trace pack` / `交互轨迹包`

What it means:
- An offline replay and debugging package.
- It contains request facts, actual tracks, events, clusters, and zone decisions.

解释：
- 用于离线回放和调试的轨迹包。
- 它包含请求事实、实际轨迹、事件、cluster 和区域决策。

### `request snapshot` / `请求快照`

What it means:
- A trace-pack copy of the request-side payload used to generate the run.
- It makes offline replay and cross-team audit self-contained.

解释：
- 被嵌入到 trace pack 中的请求侧快照，用来表示这轮运行到底是根据什么 request 产生的。
- 它的作用是让离线回放和跨团队审计尽量自包含。

### `formal draft` / `正式草案`

What it means:
- A contract candidate that is stable enough to review across teams, but not yet frozen as the final universal contract.
- A formal draft should have explicit scope and explicit non-goals.

解释：
- 指已经足够稳定，可以跨团队评审，但还没有冻结成最终通用契约的候选版本。
- 一个正式草案必须同时说明自己的适用范围，以及明确不覆盖哪些能力。

### `lifecycle line` / `生命周期线`

What it means:
- The reporting-side contract line for admission, in-flight progress, and terminal state.
- It is separate from interaction request/frame/trace.

解释：
- 表示受理、执行过程和终态结果的报告契约线。
- 它与交互侧的 request/frame/trace 分开。

### `execution_id` / `执行标识`

What it means:
- The identifier of one concrete execution attempt.
- It is not the same thing as `request_id`.

解释：
- 一次具体执行尝试的标识。
- 它不等于 `request_id`。

### `stage` / `阶段`

What it means:
- A coarse-grained runtime phase in the lifecycle/reporting line.
- Example values: `planning`, `executing`, `settling`.

解释：
- 生命周期/报告线中的粗粒度运行阶段。
- 例如：`planning`、`executing`、`settling`。

### `terminal state` / `终态`

What it means:
- The final reporting state of an execution attempt.
- Example values: `succeeded`, `failed`, `aborted`.

解释：
- 一次执行尝试最终的报告状态。
- 例如：`succeeded`、`failed`、`aborted`。

### `estimation layer` / `估测层`

What it means:
- The layer that describes what is observed now and what is predicted next.
- It does not decide intent and does not define execution bundles.

解释：
- 用来描述“现在看到了什么”和“接下来预测会变成什么”的层。
- 它不负责决定交互意图，也不负责定义执行束。

### `observation` / `观测`

What it means:
- A payload describing current subject state at one time point.
- It is the estimation-side answer to “what is visible now”.

解释：
- 描述某一时刻主体当前状态的 payload。
- 它是在估测侧回答“现在看到了什么”。

### `prediction` / `预测`

What it means:
- A payload describing future subject state at a declared horizon.
- It is the estimation-side answer to “where is this likely to be next”.

解释：
- 在给定时间跨度上描述未来主体状态的 payload。
- 它是在估测侧回答“接下来很可能会在哪里”。

### `subject` / `主体`

What it means:
- A tracked or predicted entity inside the estimation layer.
- A subject may be a target, cursor, object, or body-part related entity.

解释：
- 估测层中的被跟踪或被预测对象。
- 它可以是目标、光标、物体，或与身体部位相关的实体。

### `body keypoint` / `身体关键点`

What it means:
- A named point such as head, neck, eye, or joint carried for richer state description.
- In this repository it is an optional estimation extension, not a frozen baseline contract.

解释：
- 指诸如头部、颈部、眼部或关节等命名关键点，用来描述更丰富的状态。
- 在本仓库里它只是估测层的可选扩展，不是已经冻结的基线契约。

### `track state` / `跟踪状态`

What it means:
- A compact state describing whether a subject is directly tracked, predicted-visible, occluded, or lost.
- It belongs to the estimation layer, not to lifecycle reporting.

解释：
- 用来描述一个主体当前是被直接跟踪、预测可见、被遮挡还是已丢失的紧凑状态。
- 它属于估测层，不属于生命周期报告。

### `representation kind` / `表示形式`

What it means:
- The declared shape used to represent one subject in estimation payloads.
- Example values: `bbox2d`, `point2d`, `body_keypoints`, `hybrid`.

解释：
- 表示在估测 payload 中一个主体是用什么形式表达的。
- 例如：`bbox2d`、`point2d`、`body_keypoints`、`hybrid`。

### `body keypoint set` / `身体关键点集合`

What it means:
- A named catalog identifier for a coherent keypoint vocabulary.
- It exists so body-keypoint payloads do not drift into ad hoc local names.

解释：
- 表示一组身体关键点命名体系的目录标识。
- 它存在的目的，是避免 body keypoint payload 漂移成临时的本地命名。

### `actuation layer` / `执行层`

What it means:
- The layer that turns interaction outcomes into device-facing bundles.
- It is not the same thing as lifecycle reporting or intent planning.

解释：
- 把交互结果转成设备侧执行束的层。
- 它不等于生命周期报告，也不等于意图规划。

### `actuation bundle` / `执行束`

What it means:
- A bundle of time-ordered atoms prepared for one execution surface.
- It is the actuation-side unit of delivery.

解释：
- 面向某个执行表面、按时间排序的一组原子动作束。
- 它是执行层交付的基本单位。

### `atom` / `执行原子`

What it means:
- A smallest device-facing actuation unit inside a bundle, such as a pointer delta or a button action.
- It is an actuation term, not an interaction intent term.

解释：
- 执行束中的最小设备侧动作单元，例如指针位移或按钮动作。
- 它是执行层术语，不是交互意图术语。

### `surface kind` / `执行表面类型`

What it means:
- The device/control surface a bundle is intended for.
- Example values: `mouse`, `touch`, `gamepad`, `gear`.

解释：
- 表示一个执行束面向哪种设备或控制表面。
- 例如：`mouse`、`touch`、`gamepad`、`gear`。

### `surface profile` / `执行表面配置`

What it means:
- A reference to a named surface configuration used by an actuation bundle.
- It separates bundle semantics from device- or environment-specific tuning.

解释：
- 指向某个已命名执行表面配置的引用。
- 它把执行束语义和设备/环境相关的调优信息分开。

### `adapter ref` / `适配器引用`

What it means:
- A reference to the adapter or bridge expected to consume or report an actuation line.
- It is a traceability field, not a compatibility promise.

解释：
- 指向某个将要消费或报告 actuation 线的适配器/桥接层引用。
- 它是可追溯字段，不代表兼容承诺。

### `receipt state` / `回执状态`

What it means:
- A small actuation-side state describing whether a bundle was accepted, emitted, partially emitted, or rejected.
- It belongs to actuation feedback, not to lifecycle terminal reporting.

解释：
- 表示一个执行束在 actuation 侧是已接收、已发出、部分发出还是被拒绝的小型状态。
- 它属于 actuation 反馈，不属于生命周期终态报告。

### `reserved expansion path` / `保留扩展路径`

What it means:
- A documented rule that a future domain may land later, but no fake schema or fake registry topic is created in advance.

解释：
- 指已经写清楚未来某个域可以如何进入仓库，但不会提前伪造 schema 或 registry topic 的规则。

## Naming Rule / 命名规则

- Use contract words in schemas and APIs.
- Keep implementation words inside engines and experiments.

- Schema 和 API 使用契约词汇。
- 引擎和实验内部再使用实现词汇。

Examples:
- Contract words: `action target`, `cluster`, `zone map`, `observation`, `actuation bundle`
- Internal words: `patch`, `warhead`, `quilt`, `orbital`

示例：
- 契约词汇：`action target`、`cluster`、`zone map`、`observation`、`actuation bundle`
- 内部词汇：`patch`、`warhead`、`quilt`、`orbital`
