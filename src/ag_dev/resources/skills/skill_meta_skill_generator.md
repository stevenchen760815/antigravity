---
name: skill_meta_skill_generator
description: The Meta-Skill that defines the "Iron Standard" for creating robust, self-healing Skills.
version: 2.0 (Iron Standard)
---

# Skill Generation Protocol (Iron Standard)

## 1. Overview
This skill defines the **Mandatory Schema** for all Antigravity Skills.
Code written without this schema is considered **Legacy/Debt** and must be refactored.

## 2. The Iron Template
Every `skills/*.md` file MUST follow this structure:

```markdown
---
name: skill_concept_name  # Snake_case
description: Brief description.
version: 1.0
---

# [Skill Name]

## 1. Overview
(Why does this exist? What problem does it solve?)

## 2. Interface & Configuration
### 2.1 Prerequisities
*   **Env Vars**: List all required `.env` variables (e.g., `DB_URL`).
*   **Dependencies**: List required libs (e.g., `playwright`, `pandas`).

### 2.2 Inputs
(Function signatures or CLI arguments)

## 3. Implementation Details
(Core logic. MUST be modular and copy-paste ready.)

## 4. Self-Healing & Fallbacks (MANDATORY)
**"What if it fails?"**
*   **Scenario A**: Tool missing? -> Fallback to Native (e.g., CertUtil).
*   **Scenario B**: Auth fail? -> Trigger Human-in-the-Loop.
*   **Scenario C**: Permission denied? -> Warn and Skip.

## 5. Verification & Proof (MANDATORY)
**"How do I know it worked?"**
*   **Success**: Must return Exit Code 0 OR Non-Empty JSON.
*   **Proof**: Must generate a log line `[PROOF] <hash/status>`.

## 6. Usage Examples (Good vs Bad)
### Example A: Standard Success
(The happy path)

### Example B: Edge Case / Recovery
(The failure path handling)
```

## 3. Lifecycle Rules
1.  **Draft**: Created as `skills/new_skill.md`.
2.  **Review**: Must be reviewed by Human.
3.  **Registry**: Must be added to `skill_manifest.json`.
4.  **Immutable**: Locked after use by >2 Agents.

## 4. Quality Checklist (The Definition of Done)
*   [ ] Does it have a Fallback Strategy?
*   [ ] Does it define a Proof mechanism?
*   [ ] Does it explicitly list environmental dependencies?
*   [ ] Are the examples copy-pasteable?
