---
name: skill_project_structure
description: Defines the mandatory directory structure and file placement logic.
version: 2.0 (Iron Standard)
---

# Project Structure Governance

## 1. Overview
Enforces Protocol 11 (Structural Governance). Prevents "Root Rot" and ensures semantic organization.

## 2. Interface & Configuration
### 2.1 Prerequisites
*   **Env Vars**: None.
*   **Dependencies**: Native `os`, `pathlib`.

## 3. Directory Schema
```text
/ (Root)
├── .env                # Config (Secrets)
├── GEMINI.md           # Persona & Rules
├── task.md             # Current State
├── implementation_plan.md # Architectural Plan
├── skills/             # The Brain (Documentation/Skills)
├── scripts/            # Ops & Enforcement Tools (Non-Runtime)
├── src/                # (Optional) or DIRECT Domain Folders
│   ├── services/       # Business Logic (The Body)
│   ├── core/           # Low-level primitives
│   └── utils/          # Pure functions
└── tests/              # Verification (The Conscience)
```

## 4. Self-Healing & Fallbacks (MANDATORY)
*   **Scenario A: Missing Directory**
    *   **Action**: Agent MUST create it using `mkdir -p` or `os.makedirs(exist_ok=True)`.
    *   **Log**: `[INFO] Created missing directory: src/services`

## 5. Verification & Proof (MANDATORY)
*   **Success**: File existence check.
*   **Proof**:
    *   Run `list_dir` or `tree`.
    *   **Log**: `[PROOF] Validated structure. src/services exists.`

## 6. Usage Examples
### Example A: Placement Logic
**Bad**: Writing `crawler.py` to Root.
**Good**:
1.  Check `src/crawler/` exists? (No -> Create it).
2.  Write to `src/crawler/crawler.py`.
