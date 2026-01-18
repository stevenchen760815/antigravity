# 執法工具參考實作 (Reference Implementation)
> **來源**: Agentic Dev Playbook Appendix B
> **用途**: 為了確保協議的可執行性，以下列出標準執法腳本邏輯。Agent 應在沒有 `scripts/` 目錄的環境中，參考此邏輯進行自我審查或 **Bootstrap (還原)**。

### B.1 `pre_commit_scan.py` (Full Source)
```python
#!/usr/bin/env python3
import re
import sys
import os
from pathlib import Path
import argparse

# Protocol 7.1 "No Suffix" Policy
PROHIBITED_SUFFIXES = [r"_v\d+", r"_new", r"_backup", r"_tmp", r"_temp", r"_old"]

# Protocol 5.1 "Iron Sandbox" - Security
SECRET_PATTERNS = [
    r"(sk-[a-zA-Z0-9]{32,})",  # OpenAI Key
    r"(ghp_[a-zA-Z0-9]{30,})", # GitHub Token
    r"(gho_[a-zA-Z0-9]{30,})", # GitHub Token (OAuth)
    r"(glpat-[a-zA-Z0-9\-]{20,})", # GitLab Token
]

def check_filename(path: Path) -> list[str]:
    errors = []
    stem = path.stem
    for pattern in PROHIBITED_SUFFIXES:
        if re.search(pattern + "$", stem):
            errors.append(f"[FILENAME] Prohibited suffix '{pattern}' found in '{path.name}'")
    return errors

def check_content(path: Path) -> list[str]:
    errors = []
    try:
        # Skip binary files or huge files check could be added
        if path.stat().st_size > 1024 * 1024: # Skip > 1MB
            return errors
            
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            for pattern in SECRET_PATTERNS:
                if re.findall(pattern, content):
                    errors.append(f"[SECRET] Potential secret found in '{path.name}'")
    except Exception as e:
        # Gracefully handle read errors
        pass
    return errors

def scan_directory(root_path: Path) -> bool:
    has_error = False
    print(f"🔍 Scanning directory: {root_path}")
    
    for root, dirs, files in os.walk(root_path):
        # Ignore .git, .vscode, __pycache__
        dirs[:] = [d for d in dirs if d not in {'.git', '.vscode', '__pycache__', 'venv', 'node_modules'}]
        
        for file in files:
            file_path = Path(root) / file
            
            # Check 1: Filename
            fname_errors = check_filename(file_path)
            for err in fname_errors:
                print(f"❌ {err}")
                has_error = True
                
            # Check 2: Content
            # Only scan text-like files for secrets
            if file_path.suffix in {'.py', '.md', '.txt', '.json', '.env', '.yml', '.yaml', '.js', '.ts', '.html', '.css'}:
                content_errors = check_content(file_path)
                for err in content_errors:
                    print(f"🚨 {err}")
                    has_error = True

    return has_error

def main():
    parser = argparse.ArgumentParser(description="Agentic Dev Playbook - Pre-Commit Scan (Protocol 14.1)")
    parser.add_argument("path", nargs="?", default=".", help="Directory to scan (default: current)")
    args = parser.parse_args()
    
    root_path = Path(args.path).resolve()
    if not root_path.exists():
        print(f"Error: Path '{root_path}' does not exist.")
        sys.exit(1)
        
    found_violations = scan_directory(root_path)
    
    if found_violations:
        print("\n🚫 Scan FAILED. Violations found.")
        sys.exit(1)
    else:
        print("\n✅ Scan PASSED. No violations found.")
        sys.exit(0)

if __name__ == "__main__":
    main()
```


### B.2 `ghost_buster.py` (Full Source)
```python
#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import argparse

# Protocol 7.2 "Shadow File" Protocol
GHOST_PREFIXES = ["temp_", "tmp_", "shadow_", "debug_"]
GHOST_EXTENSIONS = [".log", ".tmp", ".bak"]

def is_ghost_file(filepath: Path) -> bool:
    name = filepath.name.lower()
    
    # Exemption: Proof of Work (Protocol 8.1)
    if name == "run_result.log" or "proof" in str(filepath.parent):
        return False
        
    # Check 1: Prefix
    for prefix in GHOST_PREFIXES:
        if name.startswith(prefix):
            return True
            
    # Check 2: Extension (Excluding logs directory if needed, but here we are strict)
    if filepath.suffix in GHOST_EXTENSIONS:
         if "log" not in str(filepath.parent): # Allow logs in log dir
             return True
             
    return False

def bust_ghosts(root_path: Path, dry_run: bool = False):
    print(f"👻 Ghost Buster searching in: {root_path}")
    ghosts_found = []
    
    for root, dirs, files in os.walk(root_path):
        # Safety: Ignore .git and critical dirs
        dirs[:] = [d for d in dirs if d not in {'.git', '.vscode', 'node_modules', 'venv', '__pycache__'}]
        
        for file in files:
            file_path = Path(root) / file
            if is_ghost_file(file_path):
                ghosts_found.append(file_path)
                
    if not ghosts_found:
        print("✅ No ghosts found. Area is clean.")
        return

    print(f"⚠️ Found {len(ghosts_found)} ghost files:")
    for ghost in ghosts_found:
        print(f" - {ghost}")
        
    if not dry_run:
        confirm = input(f"\n🔥 Delete these {len(ghosts_found)} files? (y/N): ")
        if confirm.lower() == 'y':
            for ghost in ghosts_found:
                try:
                    os.remove(ghost)
                    print(f"   Deleted: {ghost}")
                except Exception as e:
                    print(f"   Failed to delete {ghost}: {e}")
            print("🧹 Cleanup complete.")
        else:
            print("❌ Operation cancelled.")
    else:
        print("\n(Dry Run: No files were deleted)")

def main():
    parser = argparse.ArgumentParser(description="Agentic Dev Playbook - Ghost Buster (Protocol 14.2)")
    parser.add_argument("path", nargs="?", default=".", help="Directory to scan (default: current)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be deleted without doing it")
    args = parser.parse_args()
    
    root_path = Path(args.path).resolve()
    bust_ghosts(root_path, args.dry_run)

if __name__ == "__main__":
    main()
```
