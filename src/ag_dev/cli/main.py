"""
[CLI] Antigravity Main Entry Point
Purpose: Unified command line interface for all Antigravity tools.
"""
import sys
import argparse
import logging
from pathlib import Path
import shutil
import importlib.resources

# Import internal modules (formerly scripts)
# We assume they are now in the same package, but we might need to adjust their imports if they were standalone.
# For now, we will import them relative or by name if they are refactored to classes.
from .decision_router import DecisionRouter
from .skill_loader import SkillLoader
# from .system_packager import pack_system # Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [AG] - %(message)s')
logger = logging.getLogger(__name__)

def cmd_init(args):
    """Scaffold a new project in the current directory."""
    logger.info("Initializing Antigravity Project...")
    # Copy templates (in a real scenario, these would be in resources)
    # For now, we just touch the basics if they don't exist.
    
    # Check if we have resources
    try:
        # Python 3.9+ resource access
        # files = importlib.resources.files('antigravity.resources')
        # Here we simplify: Just create the folders
        Path("skills").mkdir(exist_ok=True)
        Path("rules").mkdir(exist_ok=True)
        Path("scripts").mkdir(exist_ok=True)
        Path(".env").touch(exist_ok=True)
        
        # Copy GEMINI.md if we can find it in the package
        # (This part requires proper resource packaging, skipping for minimal viable CLI)
        logger.info("Created basic structure: skills/, rules/, scripts/, .env")
        logger.info("Please read 'GEMINI.md' from the docs.")
    except Exception as e:
        logger.error(f"Init failed: {e}")

def cmd_check(args):
    """Run compliance checks (Pre-commit + Ghost Buster)."""
    logger.info("Running System Check...")
    # In a full implementation, we would call the moved pre_commit_scan.py logic here.
    # checking for pre_commit_scan existence in cli dir
    logger.info("[TODO] Porting pre_commit_scan logic integration...")

def cmd_router(args):
    """Run L0 Decision Router."""
    if args.check == 'heat':
        # Interactive mode or file input
        content = sys.stdin.read()
        res = DecisionRouter.assess_context_heat(content)
        print(res)
    else:
        # Default test
        print("Use --check heat (stdin) or --test")
        DecisionRouter().check_horizon_depth(1)

def cmd_audit(args):
    """Run L1 Skill Audit."""
    SkillLoader.scan_skills(Path("skills"))

def main():
    parser = argparse.ArgumentParser(prog="antigravity", description="Agentic Development CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Init
    subparsers.add_parser("init", help="Initialize new project")
    
    # Check
    subparsers.add_parser("check", help="Run compliance checks")

    # Router
    p_router = subparsers.add_parser("router", help="Decision Router")
    p_router.add_argument("--check", choices=['heat', 'fork', 'horizon'], help="Check type")

    # Audit
    subparsers.add_parser("audit", help="Audit Skills")

    args = parser.parse_args()

    if args.command == "init":
        cmd_init(args)
    elif args.command == "check":
        cmd_check(args)
    elif args.command == "router":
        cmd_router(args)
    elif args.command == "audit":
        cmd_audit(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
