"""
[L0] Decision Router (Fast Thinking)
Purpose: Implements the 'Architecture Decision Architect' logic (Skill V2.0).
Doc: skills/skill_decision_architecture.md
"""
import sys
import logging

# Configure Logging (Fallback to Console)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [DECISION_ROUTER] - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DecisionRouter:
    """
    The L0 Master Router.
    decisions:
    1. Context Heat (Inline vs Split)
    2. Taxonomy Check (Fork vs Keep)
    3. Horizon Check (Stop vs Continue)
    """

    @staticmethod
    def assess_context_heat(content: str, line_limit: int = 100) -> str:
        """
        Rule: If content > 100 lines, it is 'Cold' (Split).
        Otherwise, it is 'Hot' (Inline).
        """
        try:
            line_count = len(content.splitlines())
            if line_count > line_limit:
                logger.info(f"Heat Check: Cold (Lines: {line_count} > {line_limit})")
                return "SPLIT"
            logger.info(f"Heat Check: Hot (Lines: {line_count} <= {line_limit})")
            return "INLINE"
        except Exception as e:
            logger.error(f"Heat Check Error: {e}")
            return "SPLIT" # Fallback to Safe

    @staticmethod
    def check_taxonomy_fork(task_items: list, limit: int = 7) -> str:
        """
        Rule: If task items > 7, 'FORK' to new top-level task.
        Otherwise, 'KEEP' as sub-items.
        """
        try:
            count = len(task_items)
            if count > limit:
                logger.info(f"Taxonomy Check: FORK (Items: {count} > {limit})")
                return "FORK"
            logger.info(f"Taxonomy Check: KEEP (Items: {count} <= {limit})")
            return "KEEP"
        except Exception as e:
            logger.error(f"Taxonomy Check Error: {e}")
            return "FORK" # Fallback to Safe

    @staticmethod
    def check_horizon_depth(current_depth: int, max_depth: int = 4) -> str:
        """
        Rule: If nesting depth > 4, 'STOP' (Rabbit Hole).
        Otherwise, 'CONTINUE'.
        """
        try:
            if current_depth > max_depth:
                logger.warning(f"Horizon Check: STOP (Depth: {current_depth} > {max_depth})")
                return "STOP"
            logger.info(f"Horizon Check: CONTINUE (Depth: {current_depth} <= {max_depth})")
            return "CONTINUE"
        except Exception as e:
            logger.error(f"Horizon Check Error: {e}")
            return "STOP" # Fallback to Safe

if __name__ == "__main__":
    # Integration Test / CLI Usage
    import argparse
    parser = argparse.ArgumentParser(description="L0 Decision Router")
    parser.add_argument("--test", action="store_true", help="Run self-test")
    args = parser.parse_args()

    if args.test:
        print("Running Self-Test...")
        router = DecisionRouter()
        
        # Test 1: Heat
        res1 = router.assess_context_heat("Line\n" * 50)
        print(f"Test 1 (50 lines): {res1}")
        
        # Test 2: Fork
        res2 = router.check_taxonomy_fork(["Item"] * 8)
        print(f"Test 2 (8 items): {res2}")
        
        # Test 3: Horizon
        res3 = router.check_horizon_depth(5)
        print(f"Test 3 (Depth 5): {res3}")

        print("[PROOF] Self-Test Completed.")
