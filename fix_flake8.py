#!/usr/bin/env python3
"""
Script to automatically fix common flake8 issues
"""
import os
import re
import glob

def fix_file(filepath):
    """Fix common flake8 issues in a Python file"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    original_content = content
    
    # Fix W293: blank line contains whitespace
    content = re.sub(r'^[ \t]+$', '', content, flags=re.MULTILINE)
    
    # Fix W291: trailing whitespace
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    
    # Fix W292: no newline at end of file
    if content and not content.endswith('\n'):
        content += '\n'
    
    # Fix W391: blank line at end of file
    content = re.sub(r'\n\n+$', '\n', content)
    
    # Save if changed
    if content != original_content:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Fixed whitespace issues in {filepath}")

def main():
    """Fix all Python files in app directory"""
    app_dir = "app"
    
    # Find all Python files
    python_files = []
    for root, dirs, files in os.walk(app_dir):
        # Skip __pycache__ directories
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    print(f"Found {len(python_files)} Python files to fix")
    
    for filepath in python_files:
        fix_file(filepath)
    
    print("✅ Fixed whitespace issues!")

if __name__ == "__main__":
    main()
