# Skill: Verification Decision QA

> **Role**: QA-Bot
> **Trigger**: Logic Router L0 (Intent: Type C)
> **Output**: Verified Status or Debt Registration.

## 1. Evidence Collection
**Goal**: Proof of Work (Null Output Trap Prevention).

1.  **Classify Output**:
    *   **Backend/Logic**: Require `run_result.log` or Exit Code 0.
    *   **Frontend/UI**: Require `skill_visual_snapshot` or Screenshot.
    *   **Config/File**: Require `CertUtil -hashfile`.
2.  **Action**: Generate the proof before calling `notify_user`.

## 2. Perfectionism Filter (Tie-Breaker)
**Goal**: Avoid "Gold Plating".

1.  **Analyze Issues**: Are remaining issues Critical (Blocker) or Minor (Polishing)?
2.  **Apply The 10-Minute Rule**:
    *   **Can it be fixed in < 10 mins?**
        *   **Yes**: Fix it now. (Do not log debt).
        *   **No**: **DEBT REGISTER**.
            *   Add to `task.md` -> `Tech Debt`.
            *   Close Task.
3.  **Critical Exception**:
    *   If it crashes the app or leaks data, **FIX NOW** regardless of time.

---

## 🔍 Examples

### Example A: The 10-Minute Rule
**Scenario**: Variable naming is slightly inconsistent (`user_id` vs `uid`).
**Decision**: "Refactoring this takes 2 minutes. I will fix it now."

**Scenario**: Need to rewrite the entire Auth modules to support OAuth.
**Decision**: "This takes > 10 mins. I will add '[Auth] Support OAuth' to Tech Debt and close current task."

### Example B: Evidence
**Bad**: "I checked the code and it looks good." (Trust me bro)
**Good**: "I ran `pytest` and here is the log showing 5/5 passed." (Proof)
