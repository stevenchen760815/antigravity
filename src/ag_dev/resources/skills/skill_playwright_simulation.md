---
name: skill_playwright_simulation
description: A SIMULATION of a complex skill generated using the Iron Standard V2.0.
version: 1.0 (Simulation)
---

# Skill: Web Automation (Playwright)

## 1. Overview
Provides robust browser automation capabilities. Designed to map frontend routes to backed data.
**Critical**: Handles WAF evasion and session persistence.

## 2. Interface & Configuration
### 2.1 Prerequisites
*   **Env Vars**:
    *   `HEADLESS_MODE=true` (Default)
    *   `CHROME_USER_DATA_DIR=C:\Users\steve\AppData\Local\Google\Chrome\User Data`
*   **Dependencies**: `pip install playwright && playwright install chromium`

### 2.2 Inputs
*   `browse_url(url: str, selector: str = None)`
*   `capture_snapshot(name: str)`

## 3. Implementation Details
(Simplified for Simulation)
*   **Browser Context**: MUST persist cookies to avoid repeated logins.
*   **Stealth**: Use `user_agent` rotation if WAF detected.

## 4. Self-Healing & Fallbacks (MANDATORY)
*   **Scenario A: Headless Detection (WAF)**
    *   **Trigger**: `403 Forbidden` or "Verify you are human".
    *   **Action**: Switch to **Headed Mode** (`headless=False`) automatically.
    *   **Log**: `[WARN] WAF Detected. Switched to Headed Mode.`
*   **Scenario B: Selector Not Found**
    *   **Trigger**: Timeout > 5s.
    *   **Action**: Dump HTML to `debug/dump.html` and Screenshot to `debug/shot.png`.
    *   **Log**: `[ERROR] Selector missing. Context saved to debug/.`

## 5. Verification & Proof (MANDATORY)
*   **Success**: `page.title()` matches expected regex.
*   **Proof**:
    *   **Log**: `[PROOF] Page Title: "Shopee Dashboard" (Length: 1024 bytes)`
    *   **File**: `proof/snapshot_success.png` hash must be generated.

## 6. Usage Examples
### Example A: Standard Login
```python
browser = launch(headless=True)
page.goto("shopee.com")
# ... automatic proof generation
```

### Example B: WAF Recovery
```python
try:
    page.goto("shopee.com")
except WAFError:
    # Auto-fallback logic triggers here
    browser = launch(headless=False) # Visual mode
    notify_user("Please solve CAPTCHA manually.")
```
