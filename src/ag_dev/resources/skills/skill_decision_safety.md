# Skill: Safety Decision Officer

> **Role**: Security-Bot
> **Trigger**: Logic Router L0 (Intent: Type B)
> **Output**: Go/No-Go for Tool/Action.

## 1. Tool Adoption Protocol
**Goal**: Safe use of new tools.

1.  **Check Manifest**: Is tool in `skill_manifest.json`?
    *   **Yes**: GO.
    *   **No**: **AUDIT**.
        *   Run `read_resource` (Docs).
        *   **Integrity Check**:
            *   *Option A*: Run `verify_integrity.py` (Preferred).
            *   *Option B (Fallback)*: Use native `CertUtil -hashfile <file> SHA256`.
        *   *Then* GO.

## 2. Error Loop Breaker
**Goal**: Stop infinite retries.

1.  **Check History**: How many times has this error occurred consecutively?
2.  **Evaluate**:
    *   **Count < 2**: **RETRY** (Use different params/strategy).
    *   **Count >= 2**: **KILL SWITCH**.
        *   Action: Stop Execution. `notify_user` for intervention.

## 3. Destructive Op Guard
**Goal**: Prevent data loss.

1.  **Identify Target**: Is it `shadow_*`, `temp_*`, or User Code?
    *   **Shadow**: **ALLOW** (Auto-cleanup).
    *   **User Code**: **AUDIT**.
        *   Check Git Status (Clean?).
        *   Check Permissions.

## 4. Session Health Protocol (Kill Switch)
**Goal**: Prevent Context Amnesia (Turn Count > 25).

1.  **Check Turn Count**: Is it > 25?
2.  **Action (Soft Stop)**:
    *   **Step 1: Checkpoint**: Update `task.md`, mark current item `[/]`, fill `Tech Debt`.
    *   **Step 2: Cleanup**: Delete `shadow_*` and `temp_*`.
    *   **Step 3: Handover**: Output the **Resumption Prompt**.
    *   **Step 4: Stop**: Refuse further tool execution.

---

## 🔍 Examples

### Example A: Native Fallback (Tool Adoption)
**Action**: "Script not found. I will use `CertUtil` directly to verify the download."

### Example B: Error Loop
**Bad**: "Error 500. Retrying..." (Infinite Loop)
**Good**: "Error 500 occurred twice. I am stopping. User, please check server."

### Example C: The Handover Prompt (Soft Stop)
**Trigger**: Turn Count = 26.
**Output**:
> 🛑 **Session Limit Reached (Soft Stop)**
> Context is too long. Please start a new session with this command:
>
> ```text
> /resume --context "task.md" --status "Implementing Auth" --next "Verify Token Logic"
> ```
