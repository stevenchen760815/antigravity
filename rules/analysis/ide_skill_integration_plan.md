# Strategy: Integrating IDE Capabilities into Agentic Workflows
> **Objective**: Bridge the gap between "Professional Human IDEs" (Visual/Stateful) and "Agentic Workflows" (Text/Stateless).
> **Core Philosophy**: Agents do not need GUIs. They need **Structured Information** that mimics the *insight* a GUI provides.

## 1. The Translation Layer (Human Tool ➡️ Agent Skill)

We will map top-tier IDE features to specific Agent Skills.

### Category A: Intelligence & Navigation (The Brain)
*   **Human Tool**: `Go to Definition` / `Find References` (Intellisense).
*   **Agent Gap**: `grep` is dumb/noisy. It misses context.
*   **Solution**: **`skill_impact_analysis` (The 5th Seed Skill)**.
    *   *Logic*: combining `fd` (File Finding) + `grep` (Symbol Search) + `AST Parsing` (Context).
    *   *Output*: A Markdown graph of dependencies (`A imports B`).

### Category B: Data & Backend (The State)
*   **Human Tool**: DataGrip / TablePlus (Visual DB Editor).
*   **Agent Gap**: Blindly writing SQL. Guessing Schema.
*   **Solution**: **`skill_db_inspector`**.
    *   *Command*: `inspect_table users`.
    *   *Output*: Markdown Table of Columns, Types, Foreign Keys, and the first 5 rows (Preview).
    *   *Benefit*: Agent "sees" the data before writing `SELECT`.

*   **Human Tool**: Postman / Thunder Client (API Collections).
*   **Agent Gap**: `curl` one-offs. No memory of auth tokens.
*   **Solution**: **`skill_api_tester`**.
    *   *Logic*: Maintains a local `.env.test` (State). Stores usage examples in `docs/api_examples.md` (Collection).
    *   *Command*: `test_endpoint /login --save-token`.

### Category C: Frontend & Visuals (The Eye)
*   **Human Tool**: Chrome DevTools / Live Preview.
*   **Agent Gap**: Blind coding React components.
*   **Solution**: **`skill_visual_snapshot`** (via Browser Agent).
    *   *Logic*: Render component -> Capture Screenshot -> Save to `artifacts/snapshots/`.
    *   *Benefit*: Agent "sees" the layout (via user feedback or future Vision capability).

---

## 2. Integration into Genesis Roles
How do we force Agents to use these?

### The Tech Lead (Agent B): The "Intellisense" operator
*   **New Protocol**: **"Pre-Flight Inspection"**.
    *   Before writing code, Agent B MUST run `skill_impact_analysis` on the target files.
    *   *Analogy*: This is the Agent clicking "Find References" before deleting a function.

### The Architect (Agent A): The "Schema" operator
*   **New Protocol**: **"Data First"**.
    *   Agent A uses `skill_db_inspector` to generate `schema_current.md`.
    *   All planning is based on *actual* DB state, not memory.

### The Builder (Agent C): The "Test" operator
*   **New Protocol**: **"Evidence-Based Commit"**.
    *   Backend Task: Must include `skill_api_tester` output (JSON).
    *   Frontend Task: Must include `skill_visual_snapshot` path.

---

## 3. Implementation Roadmap

### Phase 1: The Core (Immediate)
*   [x] **Seed 5**: Implement `skill_impact_analysis`. (Already in Playbook V2.5).
*   [ ] **Action**: Create the physical `skills/skill_impact_analysis.md` file.

### Phase 2: The Data Layer (Next Sprints)
*   [ ] **Skill**: Create `skill_db_inspector.md`.
    *   *Tech*: Python script wrapping `sqlite3` or `sqlalchemy` reflection.
*   [ ] **Skill**: Create `skill_api_tester.md`.
    *   *Tech*: `pytest` + `requests` wrapper with explicit Token management.

### Phase 3: The Workflows (Governance)
*   [ ] **Update Playbook**: Add "Pre-Flight Inspection" to Tech Lead Protocols.
*   [ ] **Update Playbook**: Add "Evidence-Based Commit" to Builder Protocols.

---

## 4. Conclusion
We don't need to give Agents VS Code.
We need to give them **Skills that generate VS Code-like insights** in Markdown format.
*   Intellisense -> Dependency Graph (MD)
*   Database View -> Schema Table (MD)
*   Postman -> Response JSON (MD)
