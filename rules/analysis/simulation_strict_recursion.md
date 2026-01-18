# Simulation Report: The "Strict Recursion" Stress Test
> **Scenario**: Building a "Dynamic Promotion Engine" (E-commerce).
> **Goal**: Validate if "3 Agents + 4 Skills" can handle recursive branching without collapsing into chaos or producing "shallow" code.

## 🎭 The Setup: The "Deceptively Simple" Request

**User Request**:
> "I need a discount system. Users can enter a code at checkout to get a percentage off. Also need a dashboard to manage codes."

**Legacy Agent Response (The Failure)**:
*   Creates `Discount` table: `code`, `amount`.
*   Adds `input` field to Checkout.
*   **Result**: 
    1.  Fails when user asks "Can I do Buy One Get One?" (Schema too shallow).
    2.  Fails when user asks "Can I limit this to VIPs?" (No User integration).
    3.  Fails when user asks "Can I set an expiry date?" (No Date handling).

---

## ⚔️ The Simulation Log (Antigravity V2)

### Phase 1: The Architect's Blockade (Schema-First)

**Agent A (Architect)** activates.
**Skill Used**: `skill_project_structure` & `implementation_plan`.

**Internal Monologue (Thought Process)**:
> "User asked for 'Percentage Off'. But 'Promotion System' implies complexity. If I only build `% off`, I will be rewritten in 2 days. I must define the **Universal Promotion Model**."

**Action**:
1.  **REJECTS** coding.
2.  **GENERATES** `docs/schema_promotion.md`.
    *   Defines `PromotionType` (Fixed, Percentage, Bundle, Tiered).
    *   Defines `Constraint` (MinSpend, UserSegments, MaxUsage, Expiry).
    *   Defines `Effect` (DiscountOrder, DiscountItem, FreeShipping, AddGift).
3.  **Prompt to User**:
    > "I have drafted a domain model covering BOGO, VIP-only, and Validity Periods. Please review before I write a single line of UI."

**Outcome**: **Shallow Planning Averted**. The definition of "Done" moved from 2 fields to 15 fields.

### Phase 2: The Recursion Explosion (Task Forking)

**Agent A** analyzes the approved Schema.
**Observation**: "Implementing this Schema requires changes in 4 different systems."

**Action**: Trigger Protocol 11.4 (Task Taxonomy).

**Task Forking**:
*   **Parent**: `[Promo] Implement Dynamic Engine`
    *   **Child 1**: `[Promo/DB] Migration for Poly-morphic Rules` (Target: Postgres JSONB).
    *   **Child 2**: `[Promo/Cart] Recalculation Service` (The Math Core).
    *   **Child 3**: `[Promo/Admin] Rule Builder UI` (The React Form).
    *   **Child 4**: `[Promo/Checkout] Apply & Validate Endpoint` (The API).

**Risk**: **Infinite Branching**. Child 3 (Rule Builder) is massive.
**Mitigation**: **Recursive Fork**. "Child 3" is promoted to a Parent Task.
*   **New Parent**: `[Promo/Admin] Implement Rule Builder`
    *   **Sub-1**: `[UI] Condition Selector Component`.
    *   **Sub-2**: `[UI] Effect Configurator Component`.

**Outcome**: **Complexity Managed**. The "God Task" is shattered into manageable, atomic instructions for the Builder Agent. 

### Phase 3: The Builder & The Ripple Check (Consistency)

**Context**: **Agent C (Builder)** is implementing `Child 2` (Calculation Service).

**Action**: Agent C adds a new field `max_discount_amount` (Cap) to the logic.
**Code Change**: Updates `services/calculator.py`.

**Handover to Agent B (Tech Lead)**.
**Skill Used**: `skill_codebase_search` ("Ripple Check").

**Agent B Analysis**:
> "Builder added `max_discount_amount` to logic.
> I am scanning for references to 'Promotion' model...
> 1. `database/models.py`: **MISSING**.
> 2. `schemas/api_response.py`: **MISSING**.
> 3. `frontend/types.ts`: **MISSING**."

**Action**: **REJECTION**.
> "Task Failed. You introduced logic for `max_discount_amount` but the Data Model and Types are out of sync. Fixing logic is not enough. You must enforce Consistency."

**Outcome**: **Ripple Failure Averted**. The PR is blocked until the "Toothpaste" is fully squeezed out across the stack.

---

## ⚠️ Hidden Risks Identified (The "Deep" Dangers)

Even in this strict mode, new dangers emerge:

### 1. Context Amnesia (The "Why are we doing this?" Risk)
*   **Scenario**: At Step 15 (building `ConditionSelector.tsx`), Agent C focuses so hard on "React Props" that it forgets the `Constraint` Schema defined in Step 1.
*   **Symptom**: The UI looks good but generates JSON that the Backend can't parse.
*   **Patch**: **"Anchor Injection"**. Every Task Prompt *must* include the `schema_promotion.md` as mandatory context.

### 2. The Over-Engineering Tar Pit
*   **Scenario**: Agent A designs a schema so flexible it supports "Buy 3 Red items, get 1 Blue item half off on Tuesdays".
*   **Symptom**: Implementation takes 3 weeks. User just wanted reasonable coupons.
*   **Patch**: **"YAGNI Check"**. Tech Lead must ask: "Is this flexibility explicitly requested?" If no, prune the Schema.

### 3. Dependency Deadlock
*   **Scenario**: Frontend (Child 3) waits for API (Child 4). API waits for DB (Child 1).
*   **Symptom**: Agents sit idle or mock data that becomes technical debt.
*   **Patch**: **"Linearization Protocol"**. The Architect must sort Tasks by dependency (DB -> Backend -> Frontend) in `task.md`.

---

## 🏁 Conclusion

The **Genesis Bootstrap (3 Agents + 4 Skills)** successfully handles the "Promotion Engine" stress test.

1.  **Agent A** stopped the "Simple Code" trap.
2.  **Task Forking** handled the complexity explosion.
3.  **Agent B** caught the inconsistency bug.

**Verdict**: The system works, *provided* we forcefully inject Anchor Artifacts (Schema) to prevent Context Amnesia.

---

## 🇨🇳 Chinese Summary (中文摘要)

本次模擬針對極高複雜度的「動態促銷引擎 (Promotion Engine)」進行了壓力測試，驗證 3 Agent 架構的極限。

### 測試過程
1.  **攔截淺層實作 (Phase 1)**: 當 User 要求「簡單折扣」時，**架構師 (Agent A)** 拒絕直接實作，堅持先定義包含「買一送一」、「分眾歸戶」的完整 Schema。這避免了後續的「擠牙膏」式修改。
2.  **處理任務爆炸 (Phase 2)**: 面對龐大的需求，系統啟動 **遞迴分岔 (Recursive Forking)**，將「後台介面」再拆解為「條件選擇器」與「效果設定器」，將複雜度壓低至單一 Agent 可處理的原子大小。
3.  **一致性攔截 (Phase 3)**: 當 **工兵 (Agent C)** 只改了核心算法卻忘了改 DB 與 Frontend Type 時，**技術長 (Agent B)** 透過 `Ripple Check` (漣漪檢查) 抓出不同步並攔截了提交。

### 發現的新潛藏風險
嚴格模式下，新的風險主要來自「過度分工」：
1.  **上下文健忘 (Context Amnesia)**: 工兵切太細，忘了最初的 Schema 結構。解法是強制注入 **Anchor File**。
2.  **過度設計 (Over-Engineering)**: 架構師把系統想得太完美。解法是引入 **YAGNI Check** (You Ain't Gonna Need It)。
3.  **依賴鎖死 (Dependency Deadlock)**: 前後端互相等待。解法是強制 **DB優先 (DB-First)** 的線性工單排序。
