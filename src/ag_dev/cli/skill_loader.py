"""
[L1] Skill Loader (Slow Thinking)
Purpose: Dynamically scans and validates skills in `skills/` against the Iron Standard.
Doc: skills/skill_decisions_architecture.md
"""
import os
import re
import logging
from pathlib import Path
from typing import Dict, List, Optional

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [SKILL_LOADER] - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

SKILL_DIR = Path("skills")

class SkillLoader:
    """
    Manages the lifecycle of L1 Skills.
    Responsibilities:
    1. Scan: Find all .md files in skills/
    2. Validate: Check for 'Iron Standard' compliance (Frontmatter, Proof, Fallbacks).
    3. Load: Return executable metadata.
    """

    @staticmethod
    def parse_frontmatter(content: str) -> Optional[Dict[str, str]]:
        """
        Extracts YAML-like frontmatter manually to avoid external deps.
        """
        try:
            match = re.search(r'^---\s+(.+?)\s+---', content, re.DOTALL)
            if not match:
                return None
            
            frontmatter = {}
            lines = match.group(1).split('\n')
            for line in lines:
                if ':' in line:
                    key, val = line.split(':', 1)
                    frontmatter[key.strip()] = val.strip()
            return frontmatter
        except Exception:
            return None

    @staticmethod
    def validate_iron_standard(file_path: Path) -> bool:
        """
        Checks if the skill defines Mandatory sections:
        1. Frontmatter (Name, Version)
        2. Self-Healing & Fallbacks
        3. Verification & Proof
        """
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Check 1: Frontmatter
            fm = SkillLoader.parse_frontmatter(content)
            if not fm or 'name' not in fm:
                logger.error(f"[INVALID] {file_path.name}: Missing Frontmatter/Name")
                return False

            # Check 2: Mandatory Fallbacks Section
            if "Self-Healing & Fallbacks" not in content and "Self-Healing" not in content:
                logger.error(f"[INVALID] {file_path.name}: Missing 'Self-Healing & Fallbacks' section")
                return False

            # Check 3: Mandatory Proof Section
            if "Verification & Proof" not in content:
                logger.error(f"[INVALID] {file_path.name}: Missing 'Verification & Proof' section")
                return False

            return True
        except Exception as e:
            logger.error(f"[ERROR] Could not read {file_path}: {e}")
            return False

    @staticmethod
    def scan_skills(directory: Path = SKILL_DIR) -> Dict[str, Path]:
        """
        Scans all .md files in the directory.
        Returns a dict of {skill_name: file_path} for valid skills.
        """
        valid_skills = {}
        if not directory.exists():
            logger.warning(f"Skill directory {directory} does not exist.")
            return {}

        logger.info(f"Scanning skills in {directory}...")
        
        for file_path in directory.glob("skill_*.md"):
            if SkillLoader.validate_iron_standard(file_path):
                # We assume filename is close to skill name, or use frontmatter name if parsed
                # For simplicity here, use filename stem
                skill_name = file_path.stem
                valid_skills[skill_name] = file_path
                logger.debug(f"[VALID] Loaded {skill_name}")
            else:
                logger.warning(f"[SKIP] Excluding {file_path.name} (Failed Iron Standard)")

        logger.info(f"[PROOF] Loaded {len(valid_skills)} valid skills.")
        return valid_skills

if __name__ == "__main__":
    # Integration Test / CLI Usage
    import argparse
    parser = argparse.ArgumentParser(description="L1 Skill Loader")
    parser.add_argument("--audit", action="store_true", help="Audit all skills")
    args = parser.parse_args()

    if args.audit:
        print("Starting Skill Audit...")
        loader = SkillLoader()
        skills = loader.scan_skills(Path("c:/antigravity/skills")) # Use absolute path for safety in this env
        print(f"Audit Complete. Valid Skills: {list(skills.keys())}")
