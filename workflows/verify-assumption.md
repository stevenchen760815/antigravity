---
description: 驗證假設工作流 (Verify Assumption Workflow) - v2.0 (Enhanced with System Health)
---
1. **定義假設 (Define Assumption)**
   - 明確寫下你現在「以為」的狀態是什麼 (例如：以為檔案 A 在 B 資料夾，或網路正常)。

2. **系統健康預檢 (System Health Pre-Flight)**
   - **若涉及外部連線**：執行 `ping google.com` 確認網路狀態。
   - **若涉及複雜工具**：自我檢查 JSON 參數結構是否符合 Schema (特別是 Array/Object 巢狀結構)。

3. **選擇查證工具 (Select Verification Tool)**
   - 檔案存在性 -> 使用 `list_dir` 或 `find_by_name`
   - 檔案內容 -> 使用 `view_file` 或 `grep_search`
   - 網路資訊 -> 使用 `search_web`

4. **執行查證 (Execute Verification)**
   - **務必**實際執行上述工具，不可跳過。
   
5. **比對與修正 (Compare & Correct)**
   - 根據工具回傳的「真實結果」來修正原本的假設。
   - 若假設錯誤，必須在回應中明確承認「原先假設錯誤，修正後的狀態為...」。
