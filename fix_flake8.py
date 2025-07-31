#!/usr/bin/env python3
"""
Modern script to automatically fix common flake8 issues using Python 3.13 features
"""
import re
from pathlib import Path

def fix_file(filepath: Path) -> None:
    """Fix common flake8 issues in a Python file using modern Path operations"""
    content = filepath.read_text()
    original_content = content
    
    # Modern regex fixes with combined operations
    fixes = [
        (r'^[ \t]+$', ''),           # W293: blank line contains whitespace  
        (r'[ \t]+$', ''),            # W291: trailing whitespace
        (r'\n\n+$', '\n'),           # W391: blank line at end of file
    ]
    
    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
    
    # W292: no newline at end of file
    if content and not content.endswith('\n'):
        content += '\n'
    
    # Save if changed
    if content != original_content:
        filepath.write_text(content)
        print(f"Fixed whitespace issues in {filepath}")

def main() -> None:
    """Fix all Python files using modern pathlib and list comprehensions"""
    app_dir = Path("app")
    
    # Modern approach: use pathlib.rglob() and list comprehension
    python_files = [f for f in app_dir.rglob("*.py") if "__pycache__" not in f.parts]
    
    print(f"Found {len(python_files)} Python files to fix")
    
    # Use modern for-each processing
    for filepath in python_files:
        fix_file(filepath)
    
    print("✅ Fixed whitespace issues!")

if __name__ == "__main__":
    main()
