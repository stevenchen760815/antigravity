---
description: 檔案清理與歸檔工作流 (Clean Up & Archive) - 消除數位垃圾
---
1. **掃描數位垃圾 (Scan for Clutter)**
   - 使用 `find_by_name` 搜尋以下模式：
     - `*_v[0-9]*.*` (版本號檔案)
     - `*_temp.*`, `*_tmp.*` (暫存檔)
     - `*_backup.*`, `*.bak` (備份檔)
     - `*_old.*` (舊檔)

2. **分類決策 (Classify & Decide)**
   - **垃圾 (Trash)**: 純粹的暫存或錯誤產物 -> **刪除 (`delete_file`)**。
   - **歷史 (History)**: 可能有參考價值的舊版 -> **歸檔 (`move` to `.archive/`)**。
     - 若 `.archive/` 不存在，則建立之。

3. **執行清理 (Execute Cleanup)**
   - 逐一處理掃描到的檔案。
   - 嚴格遵守：不留任何非必要的重複檔案在主目錄中。

4. **報告 (Report)**
   - 輸出清理結果摘要：清除數量、歸檔數量。
