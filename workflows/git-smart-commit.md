---
description: 智慧分析變更並提交 (Git Commit & Push)
---
1. 執行 `git status` 確認當前變更。
2. 執行 `git diff` 分析具體修改內容。
3. 根據 Conventional Commits 規範 (feat, fix, docs, style, refactor)，生成一個簡潔有力的 Commit Message。
4. **向使用者展示 Message 並請求確認** (這是重要的一步，防止亂寫)。
// turbo
5. 確認後，執行 `git add .`
6. 執行 `git commit -m "GENERATED_MESSAGE"`
7. 執行 `git push`
