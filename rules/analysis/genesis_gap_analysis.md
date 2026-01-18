# Genesis Bootstrap: Gap Analysis & Optimization Plan
> **Context**: Post-Mortem of the "Strict Recursion" Simulation (`simulation_strict_recursion.md`).
> **Objective**: Identify what broke, what was missing, and how to optimize the "3 Agents + 4 Skills" model.

## 🔴 Critical Gaps Identified (The "Missing Pieces")

The simulation proved the *concept* works, but revealed specific holes in the *tooling* and *process*.

### 1. The Missing 5th Skill: "Impact Analysis"
*   **The Issue**: In Phase 3 (Ripple Check), we assumed the **Tech Lead (Agent B)** could magically "find all references".
*   **Reality**: The current Genesis setup (Appendix D) includes:
    1.  `Meta Gen` (Writing Code)
    2.  `Structure` (File Location)
    3.  `Defensive IO` (Safety)
    4.  `Log` (Format)
*   **The Gap**: There is **NO** standardized skill for **"Search & Navigation"**.
*   **Consequence**: Without a `skill_impact_analysis`, Agent B relies on ad-hoc `grep`, which is flaky. It might miss `PromotionType` if it's aliased as `PromoType` in another file.
*   **Optimization**: **Must add `skill_impact_analysis`** as the 5th Mandatory Seed Skill. It defines *how* to reliably trace dependencies (e.g., "Grep + AST" or "Text Search + File Filtering").

### 2. Protocol Gap: "Context Inheritance" (The Amnesia Cure)
*   **The Issue**: As identified in the "Context Amnesia" risk, deep-level Child Tasks (Level 3+) lose connection to the Level 1 Schema.
*   **Current State**: `task.md` lists tasks hierarchically, but **Context** is usually implicit in the chat history (which scrolls away).
*   **The Gap**: No explicit rule forces the "Builder" to re-read the `schema_promotion.md` when starting a sub-sub-task.
*   **Optimization**: **Protocol 11.5 (Context Inheritance)**.
    *   *Rule*: Every Child Task in `task.md` must explicitly link to its **Parent Context Artifact**.
    *   *Format*: `- [ ] [UI] Button Component (Context: [Schema](docs/schema.md))`

### 3. Role Calibration: The "YAGNI" Gate
*   **The Issue**: The **Architect (Agent A)**, when banned from "Shallow Planning", swung too far into "Over-Engineering" (e.g., "Buy 3 Red Items on Tuesdays").
*   **The Gap**: The Architect has no "Constraint Metric". It optimizes for *Completeness*, not *Necessity*.
*   **Optimization**: Empower the **Tech Lead (Agent B)** with a **"Scope Veto"**.
    *   *Mechanism*: Agent B acts as the "Budget Officer". If the Schema implies >200 lines of code for a "Simple Feature", Agent B must trigger a **Descope Negotiation** with the User before allowing the Builder to start.

---

## 🛠️ Optimization Action Plan

To fix these, we need to upgrade the Playbook (Appendix D).

### 1. Upgrade Seed Skills (4 -> 5)
Add `skill_impact_analysis.md`:
```markdown
# Skill: Impact Analysis
## Purpose
To scientifically determine the "Blast Radius" of a code change.
## Protocol
1. **Identifier Search**: Grep the exact symbol name.
2. **Import Trace**: Check files that import the target file.
3. **Schema Check**: If DB model changes, check API DTOs and Frontend Interfaces.
```

### 2. Implement "Context Linking" in `task.md`
Update `skill_log_standard` or `task.md` template to enforce:
```markdown
- [ ] Implement Rule Engine
  - Context: [Promotion Schema](docs/schema_promotion.md) <!-- MANDATORY LINK -->
```

### 3. Refine Architect Persona
Add to `GEMINI.md` / Architect Role:
> **The "YAGNI" Prime Directive**: "You maximize Robustness, but minimize Surface Area. If a feature was not explicitly requested (e.g., 'Tuesday-only' promos), you must mark it as `Future Scope`, not `Current Requirement`."

---

## 💡 Summary

The simulation was successful, but "fragile" because it relied on the Agents "doing the right thing" implicitly.
By adding the **5th Skill (Impact Analysis)** and the **Inheritance Protocol**, we turn that implicit luck into explicit Engineering Rigor.

---

## 🇨🇳 Chinese Summary (中文摘要)

基於「嚴格遞迴模擬」的結果，我們發現 Genesis Bootstrap (3 Agents + 4 Skills) 若要完美運作，仍缺乏以下三塊拼圖：

1.  **缺少的第五技能 (The Missing 5th Skill)**:
    *   **發現**: 技術長 (Agent B) 在執行 Ripple Check 時缺乏標準工具，只能依賴不穩定的 grep。
    *   **優化**: 必須新增 **`skill_impact_analysis`** 為第 5 個種子技能。它定義了如何科學地追蹤代碼依賴 (Blast Radius)，確保「改 A 壞 B」能被精準攔截。

2.  **流程漏洞：上下文遺傳 (Context Inheritance)**:
    *   **發現**: 任務分拆過細時，底層工兵容易忘記頂層 Schema 的限制 (Context Amnesia)。
    *   **優化**: 實施 **Protocol 11.5 (Context Inheritance)**。在 `task.md` 中，每個子任務都必須強制附上「父級上下文連結」(e.g., Link to Schema)，確保知識在樹狀結構中能正確遺傳。

3.  **角色校正：YAGNI 閘門 (The YAGNI Gate)**:
    *   **發現**: 架構師 (Agent A) 容易矯枉過正，設計出過度複雜的系統。
    *   **優化**: 賦予技術長 (Agent B) **「範圍否決權 (Scope Veto)」**。若設計過度複雜 (Over-Engineering)，Tech Lead 有權觸發「刪減談判」，強迫架構師遵守 YAGNI (You Ain't Gonna Need It) 原則。
