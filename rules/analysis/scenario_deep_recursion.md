# Scenario Analysis: The "Toothpaste Effect" & Recursive Complexity
> **Context**: Addressing the user's pain points regarding "Shallow Planning" (only delivering ID/Name/Price), "Infinite Task Branching", and "Ripple Effect Failures" (DB/Code disconnect).

## 💀 The Problem: The "Minimum Effort" Trap

Why do Agents (and junior devs) interpret "Complete Product Page" as "3 Input Fields"?

### 1. The Token Conservation Bias (省力偏誤)
*   **Mechanism**: LLMs are trained on "Tutorial Code". In 90% of tutorials, a "Product" is just `id, name, price`.
*   **Result**: Unless forced, the Agent defaults to the statistical average (The Tutorial Version), not the Enterprise Version.

### 2. The Ripple Blindness (漣漪盲點)
*   **Mechanism**: Adding a field (`weight`) requires changes in: `DB Schema` -> `API Model` -> `Frontend Type` -> `UI Component` -> `Validation Logic`.
*   **Result**: The Agent updates the UI (because you asked for it) but forgets the DB (because it's out of context).

---

## 🛡️ The Antigravity Solution: Depth-First protocols

To solve this, we introduce **Fractal Planning** and the **Schema-First Mandate**.

### Solution 1: "Schema-First" to Kill Shallow Planning
**Rule**: *No UI code is allowed until the Data Model is approved.*

#### Scenario Replay: "Build a Product Edit Page"

**❌ Old Way (The Failure)**
*   User: "Build Product Edit Page."
*   Agent: "Okay!" (Writes `ProductForm.tsx` with Name/Price).
*   User: "Where is SEO?"
*   Agent: "Sorry!" (Adds SEO tags).
*   User: "Where is Inventory?"
*   Agent: "Sorry!" (Adds refined stock). --> **Toothpaste Effect**.

**✅ The Antigravity Way (Architect Agent)**
*   User: "Build Product Edit Page."
*   **Agent A (Architect)**: *Intervention*. "I cannot build the UI yet. I must define the **Domain Model** first."
*   **Action**: Architect generates `docs/schema_product.md`.
    *   **Expands Context**: "A 'Complete' Product in typical e-commerce implies:"
        *   `Basic`: Name, SKU, Barcode.
        *   `Pricing`: Base, Sale, Tiers.
        *   `Inventory`: Stock, Safety Stock, Locations.
        *   `Media`: Images, Videos, Alt Text.
        *   `SEO`: Slug, Meta Title, OG Tags.
        *   `Variants`: Color, Size matrices.
*   **Review**: User reviews the *Schema*. "Yes, this covers it."
*   **Result**: The "Definition of Done" is now locked to 50 fields, not 3. The Builder Agent *must* implement all of them.

### Solution 2: "Task Forking" for Recursive Branching
**Rule**: *If a Task has > 7 properties, it becomes a Project.*

When the Architect realizes "Product" has 6 sub-domains (SEO, Variants, etc.), the **Protocol 11.4 (Taxonomy)** triggers:

1.  **Parent Task**: `[Product] Implement Core Editor`
    *   **Sub-Task 1**: `[Product/Schema] Define DB Models` (Blocker)
    *   **Sub-Task 2**: `[Product/Media] Implement Upload Widget`
    *   **Sub-Task 3**: `[Product/Variant] Implement Matrix Generator`
    *   **Sub-Task 4**: `[Product/SEO] Implement Meta Editor`

Instead of one giant "Do it all" prompt (which fails), the Architect **Forks** the task into meaningful chunks. The **Work Queue** grows, but the *Cognitive Load per Task* shrinks.

### Solution 3: The "Ripple Check" (Consistency)
**Rule**: *Enforcement of Single Source of Truth.*

How do we ensure adding `weight` updates the DB?

*   **Tool**: `skill_codebase_search` (Smart Grep).
*   **Protocol**: **"The Reference Check"**.
    *   When modifying `ProductForm`, the Agent MUST check: "Where else is `Product` defined?"
    *   The **Tech Lead (Agent B)** runs a `grep_search` on the entity name.
    *   **Output**:
        *   `models.py` (DB)
        *   `schemas.py` (Pydantic/API)
        *   `interfaces.ts` (Frontend)
    *   **Enforcement**: The Task is not marked Done until *all* referenced files show a git diff.

---

## 🧪 Simulation: The "Recursive Expansion"

Let's apply this to your specific request: "A Main Task spawns Branch Tasks".

**User**: "I want a new 'Campaign System' (Main Task)."

**Antigravity Response (Architect)**:
1.  **Explosion**: "Campaign System" is too big.
    *   *Analysis*: Needs Rules, targeting, budget, analytics.
2.  **Breadth-First Planning**:
    *   Create `implementation_plan.md` outlines Components.
    *   **Detected Complexity**: "Targeting" involves User Segments. -> **New Risk**.
3.  **Recursive Forking**:
    *   New Task Created: `[Campaign/Targeting] Build Segment Engine`.
    *   New Task Created: `[Campaign/Budget] Build Ledger System`.
4.  **Execution Serializer**:
    *   The Agent will NOT try to do both. It pauses.
    *   "I have identified 2 massive sub-systems. I will start with **Targeting**. Is this acceptable?"

**The Key Difference**: The Agent proactively **Refuses** to do everything at once. It breaks the "Infinite Loop" by turning it into a "Serialized List".

---

## 🇨🇳 Chinese Summary (中文摘要)

針對您提出的「牙膏式產出 (Toothpaste Effect)」、「遞迴分支發散」與「代碼不一致 (Ripple Failure)」三大痛點，Antigravity V2 的解決方案如下：

1.  **拒絕淺層思考 (Schema-First)**:
    *   **現狀**: Agent 為了省力，預設給出「教學範例等級」的 3 個欄位 (ID/Name/Price)。
    *   **新法**: **架構師 (Architect)** 被禁止直接寫 UI。必須先產出 **Schema/Domain Model** 文件。在定義出包含 SEO、庫存、多規格等 50+ 欄位的「全貌」之前，不允許進入編碼階段。

2.  **管理遞迴複雜度 (Task Forking)**:
    *   **現狀**: 一個指令涵蓋太多，導致 Agent 顧此失彼。
    *   **新法**: 當「商品編輯」被分析出含有 >7 個子領域 (如 SEO, Media, Variants) 時，Protocol 11.4 強制將其 **Fork** 為多個獨立子任務。雖增加了任務條目，但確保了每個子系統的「執行深度」。

3.  **強制一致性 (Ripple Check)**:
    *   **現狀**: 只改了 UI，忘了改 DB。
    *   **新法**: **技術長 (Tech Lead)** 執行「引用檢查」。修改 Schema 時，自動 Grep 找出前後端所有定義檔，強制全部都要有 Git Diff 才能結案。

這套機制的核心在於 **「先定義全貌 (Model)，再切割執行 (Task)，最後一致性檢查 (Check)」**，從根本上杜絕了「擠牙膏」與「改A壞B」的問題。
