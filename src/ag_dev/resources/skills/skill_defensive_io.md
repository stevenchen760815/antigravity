---
name: skill_defensive_io
description: Patterns for robust, atomic, and safe file operations.
version: 2.0 (Iron Standard)
---

# Defensive I/O Protocol

## 1. Overview
Ensures data integrity and system stability during file operations.
Enforces Protocol 5.1 (Iron Sandbox).

## 2. Interface & Configuration
### 2.1 Prerequisites
*   **Deps**: `os`, `json`, `shutil`.

## 3. Core Patterns (Implementation)
### 3.1 Atomic Write (Safe Save)
```python
def atomic_save(filepath, data):
    temp_path = f"{filepath}.tmp"
    try:
        with open(temp_path, 'w') as f:
            json.dump(data, f)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp_path, filepath)
    except PermissionError:
        # Fallback Logic Here
        print(f"[WARN] Permission Denied: {filepath}. Writing to ./tmp/ instead.")
        os.makedirs("./tmp", exist_ok=True)
        # ... fallback write ...
```

## 4. Self-Healing & Fallbacks (MANDATORY)
*   **Scenario A: Permission Denied**
    *   **Action**: Write to `./tmp/fallback_<timestamp>.json` and notify user.
    *   **Log**: `[WARN] Access Denied. Saved to Fallback Location.`
*   **Scenario B: Disk Full**
    *   **Action**: Dump critical data to `stderr` (Console) so it is captured in logs.

## 5. Verification & Proof (MANDATORY)
*   **Success**: Target file exists and hash matches.
*   **Proof**:
    *   `[PROOF] File Saved. SHA256: a1b2...`

## 6. Usage Examples
### Example A: Standard Save
`atomic_save("config.json", config)` -> OK.

### Example B: Locked File
`atomic_save("system.lock", data)` -> `PermissionError` -> `[WARN] Saved to ./tmp/system.lock.tmp`.
