# Skill: Architecture Decision Architect

> **Role**: Archi-Bot
> **Trigger**: Logic Router L0 (Intent: Type A)
> **Output**: Decision (Inline vs Split, Fork vs List)

## 1. Context Heat Check (The "Split" Decision)
**Goal**: Determine if code belongs in `task.md` or a file.

1.  **Analyze Context**: Is this exploring/debating (Hot) or implementing (Cold)?
2.  **Apply Rule 11.3**:
    *   **Hot**: Keep content **Inline** (in `task.md` or response).
    *   **Cold**: **Split** to `src/` or `services/`.
3.  **Ambiguity Breaker**:
    *   If > 100 lines -> **Split**.
    *   If imported by others -> **Split**.

## 2. Taxonomy Check (The "Fork" Decision)
**Goal**: Determine if the task checklist is manageable.

1.  **Count Items**: Look at the current `task.md` sub-list.
2.  **Evaluate**:
    *   **Count > 7**: **FORK**. Create a new Top-Level Task.
    *   **Count <= 7**: **KEEP**. Maintain as sub-items.

### ⚠️ Protocol 11.5 Mandate (Context Inheritance)
**IF you decide to FORK:**
*   You **MUST** explicitly link the Parent Context in the new task item.
*   **Format**: `- [ ] Task Name (Context: [Schema](url))`
*   **Reason**: Prevent "Context Amnesia" in the child task.

## 3. Horizon Check (The "Recursion" Decision)
**Goal**: Prevent "Rabbit Hole" depth.

1.  **Check Depth**: What is the nesting level? (e.g., Task > Sub > Sub-Sub).
2.  **Evaluate**:
    *   **Depth > 4**: **STOP**.
        *   Action: Define Mock Interface -> Request New Session.
    *   **Depth <= 4**: **CONTINUE**.

---

## 🔍 Examples

### Example A: Forking Correctly
**Bad**:
`- [ ] Implement User Login` (Where is the schema? What fields?)
**Good**:
`- [ ] [Auth] Implement User Login (Context: [UserSchema](docs/schema.md))`

### Example B: Inline vs Split
**Bad**: Dumping 200 lines of Python into a chat message "just to test".
**Good**: "The logic is >100 lines. I will write it to `services/temp_test.py` first."
