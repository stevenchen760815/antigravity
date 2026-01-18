---
description: 專案健康檢查工作流 (Project Health Check) - 預防載入與配置錯誤
---
1. **環境配置檢查 (Environment Config Check)**
   - 檢查根目錄是否包含關鍵設定檔： `package.json`, `.env`, `requirements.txt` 等。
   - 使用 `list_dir` 確認上述檔案存在。

2. **依賴與擴充檢查 (Dependencies & Extensions)**
   - **Extension Safety**: 若 Task 需要特定擴充功能 (如 ESLint, Prettier)，先檢查 `.vscode/extensions.json` (若有) 或確認環境變數。
   - 若發現 "Error while fetching extensions" 警訊，提示使用者檢查網路或改用手動安裝。

3. **Workspace 完整性 (Workspace Integrity)**
   - 檢查關鍵目錄結構 (`src`, `lib`, `components`) 是否符合預期。
   - 若 `list_dir` 回傳異常 (空目錄或權限錯誤)，立即停止並報告。

4. **報告 (Report)**
   - 輸出簡短的健康診斷報告： [PASS] / [FAIL]。
