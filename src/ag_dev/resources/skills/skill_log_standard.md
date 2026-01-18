---
name: skill_log_standard
description: Standardized logging format for cross-agent communication.
version: 2.0 (Iron Standard)
---

# Log Standard Protocol

## 1. Overview
Enforces Protocol 2 (IDE Survival). Logs must be parsable.

## 2. Interface & Configuration
### 2.1 Log Levels
`P0 (CRITICAL)`, `P1 (ERROR)`, `P2 (WARN)`, `INFO`, `DEBUG`.

## 3. Implementation Details
Use `logging` library.
Format: `[TIMESTAMP] [LEVEL] [TAG] Message`

## 4. Self-Healing & Fallbacks (MANDATORY)
*   **Scenario A: Log File Locked / Disk Full**
    *   **Action**: Fallback to `sys.stderr` (Console Stream). Verified by IDE capture.
    *   **Code**: `logging.StreamHandler(sys.stderr)` MUST be configured as backup.

## 5. Verification & Proof (MANDATORY)
*   **Success**: Log line appears in stream.
*   **Proof**:
    *   Tag `[PROOF]` is reserved for verified operations.
    *   Example: `logger.info(f"[PROOF] File created. Hash: {h}")`

## 6. Usage Examples
### Example A: Zero Trust Logging
**Bad**: `print("Done")`
**Good**: `logger.info("[PROOF] Task Completed. Output Hash: 8f3a...")`

### Example B: Secret Scrubbing
**Bad**: `logger.info(f"Key: {api_key}")`
**Good**: `logger.info(f"Key: {api_key[:4]}***")`
