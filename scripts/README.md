# Deployment Scripts

This directory contains scripts for development environment setup and cloud deployment of the portfolio application.

## 🔧 Environment Configuration

### Environment Files Setup

This directory uses environment-specific configuration files for secure and flexible deployment:

#### `.env.example` (Template - Safe to Commit)
- Contains empty values and comprehensive documentation
- **Copy this file** to create your environment-specific configurations
- Reference for all available configuration options

#### `.env.development` (Git Ignored)
- Your local development settings
- Copy from `.env.example` and fill in development values
- Used by development scripts

#### `.env.production` (Git Ignored)
- Your production deployment settings
- Copy from `.env.example` and fill in production values
- Used by production deployment scripts

### Quick Setup
```bash
# Copy template files
cp .env.example .env.development
cp .env.example .env.production

# Edit with your values
nano .env.development    # Add development settings
nano .env.production     # Add production settings
```

### Required for GCP Deployment
- `GCP_PROJECT_ID` - Your Google Cloud project ID
- `GCP_REGION` - Deployment region (e.g., "us-central1")
- `ARTIFACT_REGISTRY` - Container registry name

**Security Note**: Only `.env.example` is committed to git. Actual environment files are automatically ignored for security.

## 🚀 Available Scripts

### `setup-env.sh`
Sets up local Python development environment with Flask dependencies.

**Purpose**: Development environment initialization and Flask server setup
**Prerequisites**: 
- Python 3.8+ installed and available as `python3`
- Execute from project root directory (not from scripts/)

**Usage**:
```bash
# From project root directory
./scripts/setup-env.sh
```

**Features**:
- ✅ Clean virtual environment creation with dependency cleanup
- ✅ Automatic package installation from pyproject.toml
- ✅ Flask installation verification and version reporting
- ✅ Development workflow instructions and guidance
- ✅ Automatic Flask development server startup
- ✅ Error handling with helpful troubleshooting guidance

**What it does**:
1. Validates project directory structure (checks for pyproject.toml)
2. Removes any existing virtual environment for clean setup
3. Creates fresh Python virtual environment (`venv/`)
4. Upgrades pip and installs project dependencies
5. Verifies Flask installation and provides usage instructions
6. Automatically starts the Flask development server

### `deploy-gcp.sh`
Builds and deploys Docker images to Google Cloud Artifact Registry.

**Purpose**: Local development and testing deployments to GCP
**Prerequisites**: 
- Docker installed and running
- Google Cloud CLI (gcloud) authenticated
- Environment variables configured (see `.env.deployment`)

**Usage**:
```bash
# Set up environment
cp .env.deployment .env
# Edit .env with your GCP configuration

# Run deployment
./scripts/deploy-gcp.sh
```

**Environment Variables Required**:
- `GCP_PROJECT_ID`: Your Google Cloud Project ID
- `GCP_REGION`: Target GCP region (e.g., us-central1)
- `ARTIFACT_REGISTRY`: Artifact Registry repository name
- `DOCKER_IMAGE_NAME`: Docker image name (optional, defaults from pyproject.toml)

**Features**:
- ✅ Environment variable validation
- ✅ Docker and gcloud prerequisite checks
- ✅ Automatic image tagging for Artifact Registry
- ✅ Detailed logging and error handling
- ✅ DRY configuration using pyproject.toml defaults

## 🔧 Design Principles

### Development First
- **Local Setup**: `setup-env.sh` provides one-command development environment setup
- **Dependency Management**: Automatic virtual environment and package installation
- **Developer Experience**: Clear instructions and automatic server startup
- **Error Handling**: Helpful validation and troubleshooting guidance

### Cloud-Agnostic Architecture
- Scripts use environment variables for cloud-specific configuration
- No hardcoded cloud provider assumptions in the application code
- Easy to extend for other cloud providers (AWS, Azure)

### Security First
- All sensitive configuration via environment variables
- No credentials or project IDs in committed code
- Validation of required environment variables before deployment

### DRY Configuration
- Defaults pulled from `pyproject.toml` to avoid duplication
- Environment variables override defaults for deployment flexibility
- Single source of truth for application metadata

### Developer Experience
- Clear error messages with suggested fixes
- Colored output for easy scanning of logs
- Prerequisite validation before attempting operations
- Detailed success summaries with next steps

## 🏗️ Future Enhancements

These scripts are designed for local development and testing. For production deployments, consider:

- **GitHub Actions**: Automated CI/CD pipelines
- **Google Cloud Build**: Native GCP build and deploy automation
- **Multi-environment support**: Separate dev/staging/prod configurations
- **Rollback capabilities**: Version tagging and deployment history

## 🛠️ Troubleshooting

**Development Setup Issues (`setup-env.sh`)**:

1. **"pyproject.toml not found"**
   - Ensure you're running from project root: `./scripts/setup-env.sh`
   - Verify project structure is intact

2. **"Python 3.8+ is required"**
   - Install Python 3.8+: `brew install python@3.9` (macOS)
   - Verify installation: `python3 --version`

3. **"Failed to create virtual environment"**
   - Check Python installation: `which python3`
   - Ensure sufficient disk space
   - Try manual creation: `python3 -m venv test-venv`

4. **"Flask installation verification failed"**
   - Check network connectivity for pip downloads
   - Try manual install: `pip install flask`
   - Verify pyproject.toml dependencies are correct

**Cloud Deployment Issues (`deploy-gcp.sh`)**:

1. **"Docker daemon not running"**
   - Start Docker Desktop or Docker service
   - Verify with: `docker info`

2. **"Not authenticated to Google Cloud"**
   - Run: `gcloud auth login`
   - Configure Docker: `gcloud auth configure-docker`

3. **"Missing environment variables"**
   - Copy template: `cp .env.deployment .env`
   - Fill in your GCP project details

4. **"Permission denied"**
   - Make script executable: `chmod +x scripts/deploy-gcp.sh`

**Getting Help**:
- Check script output for detailed error messages
- Verify environment variable values with the script's configuration display
- Ensure all prerequisites are properly installed and configured
