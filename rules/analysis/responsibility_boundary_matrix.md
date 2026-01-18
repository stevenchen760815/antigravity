# The Boundary Matrix: Where Agents & Skills "Stop"
> **Context**: Answering the crucial governance question: *"Is it possible to strictly define where an Agent or Skill ends?"*
> **Answer**: Yes. The boundary is defined by the **Artifact (Output)**.

## 1. The Agent Boundary Map (Who stops where?)

The "Genesis Trinity" is separated not by *intent*, but by **Write Permissions**.

| Agent Role | **The Green Zone (Responsibilities)** | **The Red Line (STOP HERE)** | **The Terminal Artifact (Output)** |
| :--- | :--- | :--- | :--- |
| **A. Architect** | 🧠 **Thinking**. Defining data models, contracts, and directory structures. | 🛑 **Coding**. Never writes logic. Never fixes bugs. Never runs tests. | `implementation_plan.md`<br>`schemas/*.md`<br>`contracts/*.yaml` |
| **B. Tech Lead** | 🛡️ **Guarding**. auditing code, enforcing rules, running integration tests, managing Mocks. | 🛑 **Building**. Never writes feature code. Never designs DB schemas. | `audit_report.md`<br>`contracts/mocks/*`<br>`Console Output (Pass/Fail)` |
| **C. Builder** | 🔨 **Making**. Implementing the Spec. Passing the Tests. | 🛑 **Deciding**. Never changes the Schema. Never refactors architecture. | `src/**/*.py`<br>`src/**/*.tsx`<br>`tests/**/*.py` |

### 🛠️ "Is this possible?" (Feasibility Check)
*   **Yes**, via **File Extension Governance**.
    *   Architect is physically blocked from touching `.py` (except inside Markdown blocks).
    *   Builder is physically blocked from touching `schema.md`.
    *   Tech Lead acts as the "Gatekeeper" of the Git Commit.

---

## 2. The Skill Boundary Map (What tool does what?)

Skills are **Passive Tools**. They provide *Capability*, not *Will*.

| Skill Name | **Scope (What it does)** | **Boundary (Where it fails)** | **Assigned Agent** |
| :--- | :--- | :--- | :--- |
| **`skill_project_structure`** | 🗺️ **GPS**. Tells you "UserAuth belongs in `services/auth`". | ❌ **Content**. Doesn't know *how* to write Auth logic. | **Architect** |
| **`skill_db_inspector`** | 👁️ **Vision**. Shows "Users table has 5 columns". | ❌ **Judgment**. Doesn't know if 5 columns are *enough*. | **Architect** |
| **`skill_impact_analysis`** | 🕸️ **Radar**. Shows "File A imports File B". | ❌ **Risk**. Doesn't know if breaking the link is *bad*. | **Tech Lead** |
| **`skill_api_tester`** | 🧪 **Probe**. Sends `POST /login` and records `200 OK`. | ❌ **Approval**. Doesn't know if the JSON body is *correct*. | **Tech Lead** |
| **`skill_visual_snapshot`** | 📸 **Camera**. Captures `header.png`. | ❌ **Design**. Doesn't know if the header is *ugly*. | **Builder (Frontend)** |
| **`skill_defensive_io`** | 🛡️ **Glove**. Writes files safely (mkdir -p). | ❌ **Logic**. Doesn't care if you write garbage text. | **Builder (Backend)** |

### 🧠 The "Decision Gap"
*   **Skills** provide **Data** (The "What").
*   **Agents** provide **Judgment** (The "So What?").
*   *Example*: `skill_impact_analysis` reports "Changing X affects 50 files." (Data). The Agent decides "That is too risky, I Veto this plan." (Judgment).

---

## 3. The 10-Layer Recursion Application

How does this apply to the "Mega Recursion" scenario?

### Layer 1-4 (The High Ground)
*   **Agent**: **Architect**.
*   **Skills**: `structure`, `db_inspector`.
*   **Stops At**: Defining the `Interface Contract` for Layer 5.

### The Boundary Event (Layer 4)
*   **Agent**: **Tech Lead**.
*   **Skills**: `impact_analysis` (Verify isolation), `api_tester` (Spin up Mock).
*   **Stops At**: Converting the Contract into a Running Mock Server.

### Layer 5-10 (The Deep Dive)
*   **Agent**: **Builder (Sub-Session)**.
*   **Skills**: `defensive_io`, `log_standard`.
*   **Stops At**: Passing the Unit Tests defined by the Tech Lead.

---

## 4. Conclusion

**Q: Is it possible to strictly enforce this?**
**A: Yes.**

The system works because the inputs and outputs are **Mutually Exclusive**:
1.  Architect inputs `User Request` -> outputs `Plan`.
2.  Tech Lead inputs `Plan + Code` -> outputs `Audit`.
3.  Builder inputs `Plan + Mock` -> outputs `Code`.

If an Agent crosses the line (e.g., Architect trying to write code), the **System Prompt (GEMINI.md)** and **Enforcement Scripts** (Pre-Commit Scan) act as the physics engine that rejects the action.
