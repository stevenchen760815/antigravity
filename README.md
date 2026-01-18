# Antigravity (ag-dev)
**Agentic Development System - Zero Gravity Protocol v2.4**

Antigravity (`ag-dev`) is a governance and tooling framework for building robust, self-correcting AI Agent systems. It enforces "The Iron Triangle" of Rules, State, and Plan.

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/steven-example/antigravity.git
cd antigravity

# Install in editable mode
pip install -e .
```

## 🛠️ Usage

The system provides a unified CLI `antigravity`.

### 1. Initialize a New Project
Scaflold a new workspace with standard structure (`skills/`, `rules/`, `scripts/`).
```bash
antigravity init
```

### 2. Decision Router (L0)
Ask the system where to put code or how to split tasks.
```bash
# Check if context is "Hot" (Inline) or "Cold" (Split)
echo "your code context here" | antigravity router --check heat
```

### 3. Skill Audit (L1)
Verify that all skills in `skills/` comply with the Iron Standard.
```bash
antigravity audit
```

## 📂 Structure

*   `src/ag_dev/cli/`: Executable tools (`router`, `loader`, `scanner`).
*   `src/ag_dev/resources/rules/`: Core protocols (`Agentic_Dev_Playbook`).
*   `src/ag_dev/resources/skills/`: Standard skill definitions.

## ⚖️ Governance

*   **Constitution**: `src/ag_dev/resources/rules/Agentic_Dev_Playbook_2026.md`
*   **Versioning**: This package follows Semantic Versioning. Current: `2.4.0`.

---
*Powered by Zero Gravity Protocol*
