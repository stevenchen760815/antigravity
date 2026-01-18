"""
[Tool] System Packager
Purpose: Create a portable zip archive of the Antigravity System (Rules + Skills + Scripts).
Excludes user-specific project data to ensure a clean template.
"""
import zipfile
import os
import datetime
from pathlib import Path

# Config
ROOT_DIR = Path("c:/antigravity")
OUTPUT_DIR = ROOT_DIR
TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d")
ZIP_NAME = f"Antigravity_System_Release_v2.4_{TIMESTAMP}.zip"

# Whitelist: Only package these Core Components
INCLUDES = [
    "GEMINI.md",
    "task.md",
    "implementation_plan.md",
    "rules",
    "skills",
    "scripts",
    "tests",
    "workflows",
    ".gitignore"
]

# Blacklist: Always exclude these (even if inside whitelisted dirs)
EXCLUDES = [
    "__pycache__",
    ".pytest_cache",
    "*.pyc",
    "*.log",
    ".env"
]

def pack_system():
    zip_path = OUTPUT_DIR / ZIP_NAME
    print(f"[PACKAGER] Creating {zip_path}...")

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for item in INCLUDES:
            item_path = ROOT_DIR / item
            
            if not item_path.exists():
                print(f"[WARN] Skipping missing item: {item}")
                continue

            if item_path.is_file():
                zf.write(item_path, arcname=item)
                print(f"[ADD] {item}")
            
            elif item_path.is_dir():
                for root, _, files in os.walk(item_path):
                    for file in files:
                        file_path = Path(root) / file
                        
                        # Check Excludes
                        if any(ex in file_path.parts for ex in ["__pycache__", ".pytest_cache"]):
                            continue
                        if file.endswith(".pyc") or file.endswith(".log"):
                            continue
                            
                        # Calculate relative path for zip structure
                        rel_path = file_path.relative_to(ROOT_DIR)
                        zf.write(file_path, arcname=str(rel_path))
                        # print(f"[ADD] {rel_path}")

    print(f"[SUCCESS] Package created: {zip_path}")
    print(f"[SIZE] {zip_path.stat().st_size / 1024:.2f} KB")

if __name__ == "__main__":
    pack_system()
