# 🌲 Decision Tree L0: The Master Router

> **Purpose**: The "Central Nervous System" of the Agent.
> **Rule**: Do not guess. Follow the Router.
> **Status**: Active (Federated Architecture)

## 0. The Intent Classifier (Start Here)
Before executing *any* task, classify your intent:

| Intent Type | Definition | Routing Target |
| :--- | :--- | :--- |
| **Type A: Architecting** | Creating files, organizing folders, splitting tasks. | 👉 **[Load Skill](..\skills\skill_decision_architecture.md)** |
| **Type B: Surviving** | Running tools, handling errors, managing tokens. | 👉 **[Load Skill](..\skills\skill_decision_safety.md)** |
| **Type C: Verifying** | Closing tasks, committing code, auditing quality. | 👉 **[Load Skill](..\skills\skill_decision_verification.md)** |

---

## 🛑 The "Stuck" Protocol
If you are unsure where to go, or if you are looping between trees:

1.  **Stop**: Do not execute tools.
2.  **Ask**: Use `notify_user` to request clarification.
    *   *Template*: "I am stuck at Decision Router L0. My intent is [Intent], but I don't fit into Type A, B, or C."
