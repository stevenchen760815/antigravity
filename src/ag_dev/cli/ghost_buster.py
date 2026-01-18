#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import argparse

# Protocol 14.2 "Ghost Buster"
GHOST_PREFIXES = ["temp_", "tmp_", "shadow_", "debug_"]
GHOST_EXTENSIONS = [".log", ".tmp", ".bak"]

def is_ghost_file(filepath: Path) -> bool:
    name = filepath.name.lower()
    
    # Exemption: Proof of Work (Protocol 7.2)
    if name == "run_result.log":
        return False
    if "proof" in str(filepath.parent).lower():
        return False
    if "logs" in str(filepath.parent).lower(): # Exclude logs dir itself if checks extension
        return False
        
    # Check Prefixes
    for prefix in GHOST_PREFIXES:
        if name.startswith(prefix):
            return True
            
    # Check Extensions (Loose check, be careful)
    # Only if not in a designated log folder (handled above somewhat, but let's be strict)
    if filepath.suffix in GHOST_EXTENSIONS:
        return True
        
    return False

def bust_ghosts(root_path: Path, delete: bool = False):
    ghosts = []
    print(f"👻 Hunting ghosts in: {root_path}")
    
    for root, dirs, files in os.walk(root_path):
        # Safety: Don't look inside .git or venv
        dirs[:] = [d for d in dirs if d not in {'.git', '.vscode', 'venv', 'node_modules', '__pycache__'}]
        
        for file in files:
            file_path = Path(root) / file
            if is_ghost_file(file_path):
                ghosts.append(file_path)
                
    if not ghosts:
        print("✨ Clean! No ghost files found.")
        return

    print(f"\nFound {len(ghosts)} ghost files:")
    for g in ghosts:
        print(f"  - {g.relative_to(root_path)}")
        
    if delete:
        print("\n💥 Busting ghosts...")
        for g in ghosts:
            try:
                os.remove(g)
                print(f"  Deleted: {g.name}")
            except Exception as e:
                print(f"  Failed to delete {g.name}: {e}")
        print("Done.")
    else:
        print("\n⚠️  Dry Run. Use --fix to delete these files.")
        # Return non-zero if ghosts exist, so CI can fail
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Agentic Dev Playbook - Ghost Buster (Protocol 14.2)")
    parser.add_argument("path", nargs="?", default=".", help="Directory to scan (default: current)")
    parser.add_argument("--fix", action="store_true", help="Automatically delete ghost files")
    args = parser.parse_args()
    
    root_path = Path(args.path).resolve()
    if not root_path.exists():
        print(f"Error: Path '{root_path}' does not exist.")
        sys.exit(1)
        
    bust_ghosts(root_path, delete=args.fix)

if __name__ == "__main__":
    main()
