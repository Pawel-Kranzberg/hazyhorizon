# Release Process

This document describes how to release new versions of hazyhorizon.

## Automated Release Setup

The project uses GitHub Actions for automated releases. When you create a new tag or GitHub release, it will automatically:

1. **Test** the code on Python 3.11 and 3.12
2. **Build** the package using uv
3. **Publish** to PyPI automatically

## Prerequisites

### 1. Set up PyPI API Token in GitHub Secrets

1. Go to your repository settings: `https://github.com/Pawel-Kranzberg/hazyhorizon/settings/secrets/actions`
2. Click "New repository secret"
3. Name: `PYPI_API_TOKEN`
4. Value: Your PyPI API token (starts with `pypi-`)

### 2. Alternative: Trusted Publishing (Recommended)

For enhanced security, you can set up trusted publishing instead of using API tokens:

1. Go to PyPI project settings: `https://pypi.org/manage/project/hazyhorizon/settings/publishing/`
2. Add a new trusted publisher:
   - Owner: `Pawel-Kranzberg`
   - Repository: `hazyhorizon`
   - Workflow: `release.yml`
   - Environment: `pypi`

Then uncomment the trusted publishing line in `.github/workflows/release.yml`.

## Release Methods

### Method 1: Using the Release Script (Recommended)

```bash
# Update version and create tag automatically
python scripts/release.py 0.2.0
```

This script will:
- Update the version in `pyproject.toml`
- Commit the change
- Create a git tag
- Push everything to GitHub
- Trigger the automated release

### Method 2: Manual Tag Creation

```bash
# 1. Update version in pyproject.toml manually
# 2. Commit the change
git add pyproject.toml
git commit -m "Bump version to 0.2.0"

# 3. Create and push tag
git tag -a v0.2.0 -m "Release 0.2.0"
git push origin main
git push origin v0.2.0
```

### Method 3: GitHub Release (Web Interface)

1. Go to `https://github.com/Pawel-Kranzberg/hazyhorizon/releases`
2. Click "Create a new release"
3. Choose or create a tag (e.g., `v0.2.0`)
4. Fill in release notes
5. Click "Publish release"

## Monitoring Releases

After triggering a release:

1. **Check GitHub Actions**: `https://github.com/Pawel-Kranzberg/hazyhorizon/actions`
2. **Verify PyPI**: `https://pypi.org/project/hazyhorizon/`
3. **Test installation**: `pip install hazyhorizon==NEW_VERSION`

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR** (1.0.0): Breaking changes
- **MINOR** (0.2.0): New features, backward compatible
- **PATCH** (0.1.1): Bug fixes, backward compatible

## Troubleshooting

### Release Failed
- Check GitHub Actions logs for errors
- Ensure PyPI token is valid and has correct permissions
- Verify version number doesn't already exist on PyPI

### Tests Failed
- Fix failing tests before releasing
- Ensure code works on both Python 3.11 and 3.12

### Build Failed
- Check that `pyproject.toml` is valid
- Ensure all dependencies are properly specified
