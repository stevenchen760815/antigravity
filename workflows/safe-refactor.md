---
description: 安全重構與原子化更新工作流 (Safe Refactor & Atomic Update) - 預防檔案損壞
---
1. **建立影子檔案 (Create Shadow File)**
   - 複製目標檔案：`copy Target.ext Target.shadow.ext`
   - **注意**：所有修改皆針對 `Target.shadow.ext` 進行，絕不觸碰原檔。

2. **執行修改 (Execute Modification)**
   - Agent 對影子檔案進行重構或功能新增。

3. **驗證與測試 (Verify & Test)**
   - 針對影子檔案執行編譯或測試指令。
   - 若測試失敗 -> **終止**，保留影子檔案供 Debug (或詢問使用者是否刪除)。

4. **原子替換 (Atomic Swap)**
   - **僅在測試通過後執行**。
   - 使用 `move /y Target.shadow.ext Target.ext` 瞬間替換。
   - 此操作確保檔案系統只會處於「舊版可用」或「新版可用」兩種狀態，不會有「壞掉的中間態」。

5. **最終清理 (Final Cleanup)**
   - 確認沒有遺留任何 `*.shadow.*` 檔案。
