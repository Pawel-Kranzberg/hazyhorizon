#!/usr/bin/env python3
"""
Release helper script for hazyhorizon package.
Usage: python scripts/release.py <version>
Example: python scripts/release.py 0.2.0
"""

import sys
import subprocess
import re
from pathlib import Path

def update_version_in_pyproject(version: str) -> None:
    """Update version in pyproject.toml"""
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text()
    
    # Update version line
    updated_content = re.sub(
        r'version = "[^"]*"',
        f'version = "{version}"',
        content
    )
    
    pyproject_path.write_text(updated_content)
    print(f"✅ Updated version to {version} in pyproject.toml")

def create_git_tag(version: str) -> None:
    """Create and push git tag"""
    tag_name = f"v{version}"
    
    # Add and commit version change
    subprocess.run(["git", "add", "pyproject.toml"], check=True)
    subprocess.run(["git", "commit", "-m", f"Bump version to {version}"], check=True)
    
    # Create tag
    subprocess.run(["git", "tag", "-a", tag_name, "-m", f"Release {version}"], check=True)
    
    # Push changes and tag
    subprocess.run(["git", "push", "origin", "main"], check=True)
    subprocess.run(["git", "push", "origin", tag_name], check=True)
    
    print(f"✅ Created and pushed tag {tag_name}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/release.py <version>")
        print("Example: python scripts/release.py 0.2.0")
        sys.exit(1)
    
    version = sys.argv[1]
    
    # Validate version format (basic check)
    if not re.match(r'^\d+\.\d+\.\d+$', version):
        print("❌ Version should be in format X.Y.Z (e.g., 0.2.0)")
        sys.exit(1)
    
    print(f"🚀 Preparing release {version}")
    
    try:
        update_version_in_pyproject(version)
        create_git_tag(version)
        
        print(f"""
🎉 Release {version} prepared successfully!

The GitHub Action will now:
1. Run tests on Python 3.11 and 3.12
2. Build the package
3. Publish to PyPI automatically

Check the progress at:
https://github.com/Pawel-Kranzberg/hazyhorizon/actions
        """)
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during release: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
