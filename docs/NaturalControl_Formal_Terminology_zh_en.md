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

## Naming Rule / 命名规则

- Use contract words in schemas and APIs.
- Keep implementation words inside engines and experiments.

- Schema 和 API 使用契约词汇。
- 引擎和实验内部再使用实现词汇。

Examples:
- Contract words: `action target`, `cluster`, `zone map`
- Internal words: `patch`, `warhead`, `quilt`, `orbital`

示例：
- 契约词汇：`action target`、`cluster`、`zone map`
- 内部词汇：`patch`、`warhead`、`quilt`、`orbital`


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
