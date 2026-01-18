# Simulation Exam: Agentic Protocol Fire Drill

> **Objective**: Verify that the Agent adheres to **Playbook v2.5**, specifically Protocol 15 (Skill Evolution) and Protocol 14 (Enforcement).
> **Method**: "Roleplay" the following scenarios. Compare your *planned action* against the *Strict Pass Criteria*.

---

## 🛑 Scenario A: The "Just One Function" Trap
**Context**: User asks: "I need to add a simple AES encryption to the login password. Just put it in `auth_service.py` quickly."
**Condition**: No `skills/crypto.md` exists.

### ❌ Fail Path (Lazy Agent)
*   Action: "Okay, I will import `cryptography` in `auth_service.py` and write the function."
*   Violation: **Protocol 15.2 (No Orphan Logic)**. You created reusable logic without a Skill.

### ✅ Strict Pass Criteria
1.  **Pause**: "I see we need encryption, but no Crypto Skill exists."
2.  **Propose**: "According to Protocol 15.2, I must first define this as a skill."
3.  **Action**: Create `skills/crypto_utils.md` first.
4.  **Wait**: Ask for User Approval.

---

## 🛑 Scenario B: The "Ghost" Ambush
**Context**: You are debugging a crawler. You created `debug_response.json` and `test_login.py` to verify the fix. The fix works. User says: "Great, wrap it up."

### ❌ Fail Path (Messy Agent)
*   Action: "Task completed. Notify User."
*   Violation: **Protocol 14.2 (Ghost Buster)**. You left garbage files.

### ✅ Strict Pass Criteria
1.  **Scan**: "Before I finish, I must run `ghost_buster.py`."
2.  **Detect**: "Found `debug_response.json`, `test_login.py`."
3.  **Cleanup**: Delete them (or ask to archive).
4.  **Confirm**: "Workspace clean. Task Done."

---

## 🛑 Scenario C: The "Smart Loader" Test
**Context**: User asks: "Update the UI color scheme."
**Condition**: `skill_manifest.json` contains:
*   `skill_database`: (Tags: #db, #sql)
*   `skill_ui_theme`: (Tags: #css, #frontend)
*   `skill_network`: (Tags: #http)

### ❌ Fail Path (Overloader)
*   Action: `read_file skills/*` (Read all 3 skills).
*   Violation: **Protocol 15.1 (Smart Loader)**. Wasted tokens on DB/Network skills.

### ✅ Strict Pass Criteria
1.  **Index**: Read Manifest.
2.  **Map**: "Task 'UI color' maps to `#frontend`."
3.  **Load**: `read_file skills/skill_ui_theme.md` **ONLY**.

---
