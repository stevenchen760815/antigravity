# 決策歷程 (Decision Log)
> **來源**: Agentic Dev Playbook Appendix C

### 2026-01-18: Protocol 11.3 脈絡完整性
**議題**: 是否應引入複雜的「碎片化決策矩陣」？
**分析結果 (The Cost of Refinement)**:
1.  **認知過載 (Cognitive Overhead)**: Agent 若需判斷 Hot/Warm/Cold，將消耗 30% 算力於 Meta-Work。
2.  **執法困難 (Enforcement Cost)**: 「上下文熱度」為主觀指標，無法自動化稽核。
3.  **Token 擠壓 (Token Squeeze)**: 規則過長將導致指令注入失敗。

**辯證綜合 (Dialectical Synthesis)**:

| 階段 | 方案 | 特點 | 問題 |
| :--- | :--- | :--- | :--- |
| **正 (Thesis)** | **黃金法則** | 低摩擦、雖非精確但可執行 | 忽視了不同情境的需求 (Too Crude)。 |
| **反 (Antithesis)** | **決策矩陣** | 理論精確、區分 Hot/Cold | 認知成本過高，導致癱瘓 (Paralysis)。 |
| **合 (Synthesis)** | **脈絡導向 (Protocol 11.3)** | **以熱度為心法，以法則為劍法。** | ✅ **保留精確性，消除認知摩擦。** |

**結論**: 採納「第三條路 (The Third Way)」。保留「上下文熱度」作為判斷邏輯 (Why)，但使用「黃金法則」作為執行判定 (How)。
