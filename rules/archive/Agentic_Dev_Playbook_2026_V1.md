# Agentic Development Playbook: "The Zero Gravity Protocol"
> **Date**: 2026-01-18
> **Scope**: Advanced Human-Agent Teaming, Long-Context Management, STG Game Architecture
> **Status**: **CONSOLIDATED DOCTRINE**

---

## 🏗️ Part 1: Architecture Blueprint (Case Study: STG Game)
對於中小型專案（如 Web 射擊遊戲）的標準架構與分工。

### 1.1 The Trinity (Agent 分工)
不要過度拆分，維持 **3 Agent 黃金比例**：

| Agent Name | Role | Personality | Key Responsibilities |
| :--- | :--- | :--- | :--- |
| **Agent A: Core** | Engine & Physics | Performance Obsessed | Game Loop, Delta Time, Object Pool, Collision, Memory Management (Zero GC) |
| **Agent B: Logic** | Gameplay & AI | Modular Thinker | Spawning Logic, Behavior Trees, Score System, Player/Weapon Stats |
| **Agent C: Visual** | Presentation | Experience Designer | Canvas/WebGL, Sprites, Animations, UI/HUD, Particle Systems (Juice) |

### 1.2 The Skill Set (原子能力)
必需封裝為獨立 Skills (e.g., `skills/*.md`)：
1.  **`skill_math_vector`**: 2D 向量運算庫 (Add, Sub, Mag, Norm)。
2.  **`skill_object_pool`**: **[CRITICAL]** 禁止 Runtime `new/delete`。強制重複使用實例。
3.  **`skill_input_system`**: 緩衝輸入 (Input Buffer) 防延遲。
4.  **`skill_state_machine`**: Menu -> Play -> Pause -> End。

### 1.3 Execution Phases (任務路徑)
1.  **Phase 1: The Heartbeat** (Loop, Delta Time, FPS Monitor).
2.  **Phase 2: The Actor** (Player Move, Border, Basic Shot).
3.  **Phase 3: The Threat** (Enemy Spawner, Basic Tracking).
4.  **Phase 4: The Interaction** (Conflict, Hitbox, Damage).
5.  **Phase 5: The Juice** (Shake, Flash, Particles, SFX).

---

## 🛡️ Part 2: The "IDE Survival" Guide
解決 IDE 開發中的「人機感官落差」與「摩擦」。

### 2.1 Four Major Frictions
1.  **The Lint Gap**: Agent 看不到紅色波浪線，導致自信提交錯誤代碼。
2.  **The Blind Painter**: Agent 看不到 Canvas 畫面，無法判斷視覺邏輯錯誤（如圖層順序）。
3.  **The Ghost Writer**: 人機同時寫入同一檔案導致 Race Condition。
4.  **The Silent Server Death**: Dev Server 崩潰但 Agent 未察覺。

### 2.2 Defense Strategies
*   **Proactive Linting**: 提交前強制執行 `npm run type-check` 或模擬編譯。
*   **Visual Debugging**: 強制實作 `Debug Overlay` (繪製 Hitbox 線框、顯示 FPS/Pos 數值)。
*   **Hands-off Protocol**: 任務執行期間 (Task Active)，人類禁止觸碰目標檔案。
*   **Log-Driven**: 使用結構化 Log 代替純文字，方便 Agent 解析狀態。

---

## ⏳ Part 3: Session Lifecycle Governance
如何管理長對話的「記憶衰退」問題。

### 3.1 The Kill Switch Metrics (何時換房)
不要依賴感覺，依賴指標：
*   **Turn Count > 25**:強制 Soft Stop。
*   **Error Loop >= 2**: 同一個 Bug 修兩次修不好 -> **立即換房**。
*   **Phase Completion**: 一個階段結束 -> 完美切點。

### 3.2 The Handover Protocol (交接術)
1.  **Atomic Scoping**: 一個 Session 只做 `task.md` 裡的一個 Checkbox。拒絕 Scope Creep。
2.  **Checkpointing**: 結束前必須更新 `task.md` 並確保程式碼處於 "Compilable" 狀態。
3.  **Context Dump** (Optional): 留下 `handover.json` 或關鍵留言給下一任 Agent。

---

## 🚀 Part 4: The "Cold Boot" Protocol
如何達成「零設定」無縫接軌 (Zero-Touch Resume)。

### 4.1 The Anchor Files (錨點)
Agent 啟動時不需對話歷史，只需讀取以下 **Source of Truth**：
*   **`GEMINI.md` / `.cursorrules`**: 包含 Persona & Coding Style。
*   **`task.md`**: 包含進度狀態 (State)。
*   **`implementation_plan.md`**: 包含架構設計 (Context)。

### 4.2 The Boot Sequence
1.  **Identity Check**: Load `GEMINI.md`.
2.  **State Check**: Load `task.md`. Find first `[ ]`.
3.  **Env Check**: Check `node_modules`.
4.  **Auto-Start**: "偵測到 Phase 1 完成。正在讀取 Phase 2 需求..."

### 4.3 Idempotency (冪等性)
*   不要盲目執行 `npm install`。
*   先 Check，再 Action。
*   確保每次啟動的行為一致，無論是第一次還是第一百次。

---
> *This document serves as the master blueprint for the Antigravity Agentic Workflow.*
