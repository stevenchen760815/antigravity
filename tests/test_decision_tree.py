"""
Unit Tests for Agentic Decision Tree (L0 + L1)
"""
import pytest
from pathlib import Path
from scripts.decision_router import DecisionRouter
from scripts.skill_loader import SkillLoader

# --- L0: Decision Router Tests ---

def test_router_heat_check_hot():
    # Less than 100 lines -> Hot (Inline)
    content = "Line\n" * 50
    assert DecisionRouter.assess_context_heat(content) == "INLINE"

def test_router_heat_check_cold():
    # More than 100 lines -> Cold (Split)
    content = "Line\n" * 101
    assert DecisionRouter.assess_context_heat(content) == "SPLIT"

def test_router_fork_keep():
    # 7 items -> Keep
    items = ["Task"] * 7
    assert DecisionRouter.check_taxonomy_fork(items) == "KEEP"

def test_router_fork_trigger():
    # 8 items -> Fork
    items = ["Task"] * 8
    assert DecisionRouter.check_taxonomy_fork(items) == "FORK"

def test_router_horizon_stop():
    # Depth 5 -> Stop
    assert DecisionRouter.check_horizon_depth(5) == "STOP"

# --- L1: Skill Loader Tests ---

def test_loader_frontmatter_parsing():
    content = "---\nname: test_skill\nversion: 1.0\n---"
    fm = SkillLoader.parse_frontmatter(content)
    assert fm is not None
    assert fm['name'] == 'test_skill'

def test_loader_validation_success(tmp_path):
    # Create a valid skill file
    p = tmp_path / "skill_valid.md"
    p.write_text("""---
name: valid_skill
---
# Test Skill
## Self-Healing & Fallbacks
...
## Verification & Proof
...
""", encoding='utf-8')
    assert SkillLoader.validate_iron_standard(p) is True

def test_loader_validation_fail_no_proof(tmp_path):
    # Create an invalid skill file (missing Proof)
    p = tmp_path / "skill_invalid.md"
    p.write_text("""---
name: invalid_skill
---
# Test Skill
## Self-Healing & Fallbacks
...
""", encoding='utf-8')
    assert SkillLoader.validate_iron_standard(p) is False
