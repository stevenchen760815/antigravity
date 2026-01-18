---
description: 對當前修改的檔案進行 Code Review
---
1. 讀取當前 git diff 或開啟的檔案。
2. 檢查以下重點：
    - 是否有安全漏洞 (Security Vulnerabilities)？
    - 是否有顯著的效能問題 (Performance Issues)？
    - 變數命名是否清晰？
    - 是否遺漏了 Error Handling？
3. 輸出一份 Markdown 格式的報告，包含：
    - 🔴 Critical Issues (必須修)
    - 🟡 Suggestions (建議修)
    - 🟢 Good Practices (值得保持)
