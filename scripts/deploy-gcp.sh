#!/bin/bash

# ============================================================================
# GCP Artifact Registry Deployment Script
# ============================================================================
#
# This script builds and deploys a Docker image to Google Cloud Artifact Registry.
# It's designed for local development and testing - production deployments should
# use GitHub Actions or Cloud Build for automated CI/CD pipelines.
#
# Features:
# - Environment variable-driven configuration for DRY, scalable code
# - Validation of required GCP setup before deployment
# - Secure handling of authentication and project configuration
# - Detailed logging for troubleshooting and monitoring
# - Fail-fast approach to prevent partial deployments
#
# Prerequisites:
# - Docker installed and running
# - Google Cloud CLI (gcloud) installed and authenticated
# - gcloud configured for Docker authentication
# - Required environment variables set (see validation section)
#
# Usage:
#   1. Set environment variables (see .env.example or .env.deployment)
#   2. Ensure you're authenticated to GCP: gcloud auth login
#   3. Configure Docker for Artifact Registry: gcloud auth configure-docker
#   4. Run: ./scripts/deploy-gcp.sh
#
# Environment Variables Required:
#   GCP_PROJECT_ID: Your Google Cloud Project ID
#   GCP_REGION: Target GCP region (e.g., us-central1)
#   ARTIFACT_REGISTRY: Artifact Registry repository name
#   DOCKER_IMAGE_NAME: Docker image name (defaults from pyproject.toml)
#
# ============================================================================

set -e  # Exit immediately on any error

# Terminal Colors for Enhanced Output
RED='\033[0;31m'      # Error messages and failures
GREEN='\033[0;32m'    # Success messages and completions
YELLOW='\033[1;33m'   # Warning messages and important info
BLUE='\033[0;34m'     # Informational messages and progress
PURPLE='\033[0;35m'   # Highlighted values and configuration
NC='\033[0m'          # No Color (reset)

# Script Header
echo -e "${BLUE}============================================================================${NC}"
echo -e "${BLUE}🚀 GCP Artifact Registry Deployment Script${NC}"
echo -e "${BLUE}============================================================================${NC}"

# Environment Setup: Load variables from .env if available
if [[ -f .env ]]; then
    echo -e "${BLUE}📁 Loading environment variables from .env file...${NC}"
    export $(grep -v '^#' .env | xargs)
fi

# Configuration Loading with DRY Defaults
echo -e "${BLUE}📖 Loading deployment configuration...${NC}"

# Helper function to extract values from pyproject.toml for DRY configuration
get_toml_value() {
    local key="$1"
    local default="$2"
    
    if command -v python3 &> /dev/null; then
        python3 -c "
import tomllib
try:
    with open('pyproject.toml', 'rb') as f:
        data = tomllib.load(f)
    value = data.get('tool', {}).get('me2u', {}).get('$key', '$default')
    print(value)
except Exception:
    print('$default')
" 2>/dev/null
    else
        echo "$default"
    fi
}

# Application Configuration (safe defaults from pyproject.toml)
APP_NAME=${APP_NAME:-$(get_toml_value "app_name" "me2u Portfolio")}
VERSION=${VERSION:-$(get_toml_value "version" "1.0.0")}
DOCKER_IMAGE_NAME=${DOCKER_IMAGE_NAME:-$(get_toml_value "container_image_name" "portfolio-app")}
IMAGE_TAG=${IMAGE_TAG:-$(get_toml_value "container_tag" "latest")}

# GCP Configuration (environment variables only for security)
GCP_PROJECT_ID=${GCP_PROJECT_ID}
GCP_REGION=${GCP_REGION}
ARTIFACT_REGISTRY=${ARTIFACT_REGISTRY}

# Derived Configuration
REGISTRY_URL="${GCP_REGION}-docker.pkg.dev"
FULL_IMAGE_URL="${REGISTRY_URL}/${GCP_PROJECT_ID}/${ARTIFACT_REGISTRY}/${DOCKER_IMAGE_NAME}:${IMAGE_TAG}"

# Display Current Configuration
echo -e "${PURPLE}📋 Deployment Configuration:${NC}"
echo -e "   • App Name: ${APP_NAME}"
echo -e "   • Version: ${VERSION}"
echo -e "   • Image Name: ${DOCKER_IMAGE_NAME}"
echo -e "   • Image Tag: ${IMAGE_TAG}"
echo -e "   • GCP Project: ${GCP_PROJECT_ID}"
echo -e "   • GCP Region: ${GCP_REGION}"
echo -e "   • Registry: ${ARTIFACT_REGISTRY}"
echo -e "   • Full Image URL: ${FULL_IMAGE_URL}"
echo ""

# Validation: Check Required Environment Variables
echo -e "${BLUE}🔍 Validating deployment prerequisites...${NC}"

REQUIRED_VARS=(
    "GCP_PROJECT_ID:Your Google Cloud Project ID"
    "GCP_REGION:Target GCP region (e.g., us-central1)"
    "ARTIFACT_REGISTRY:Artifact Registry repository name"
)

MISSING_VARS=()

for var_info in "${REQUIRED_VARS[@]}"; do
    var_name="${var_info%%:*}"
    var_description="${var_info#*:}"
    
    if [[ -z "${!var_name}" ]]; then
        MISSING_VARS+=("${var_name}: ${var_description}")
    fi
done

if [[ ${#MISSING_VARS[@]} -gt 0 ]]; then
    echo -e "${RED}❌ Missing required environment variables:${NC}"
    for var in "${MISSING_VARS[@]}"; do
        echo -e "${RED}   - ${var}${NC}"
    done
    echo -e "${YELLOW}💡 Set these in your .env file or environment${NC}"
    echo -e "${YELLOW}💡 Example: export GCP_PROJECT_ID=my-project-123${NC}"
    exit 1
fi

# Validation: Check Docker Installation and Status
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker is not installed or not in PATH${NC}"
    echo -e "${YELLOW}💡 Install Docker: https://docs.docker.com/get-docker/${NC}"
    exit 1
fi

if ! docker info &> /dev/null; then
    echo -e "${RED}❌ Docker daemon is not running${NC}"
    echo -e "${YELLOW}💡 Start Docker and try again${NC}"
    exit 1
fi

# Validation: Check Google Cloud CLI Installation and Authentication
if ! command -v gcloud &> /dev/null; then
    echo -e "${RED}❌ Google Cloud CLI (gcloud) is not installed${NC}"
    echo -e "${YELLOW}💡 Install gcloud: https://cloud.google.com/sdk/docs/install${NC}"
    exit 1
fi

# Check if user is authenticated to gcloud
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | head -n1 | grep -q "@"; then
    echo -e "${RED}❌ Not authenticated to Google Cloud${NC}"
    echo -e "${YELLOW}💡 Run: gcloud auth login${NC}"
    exit 1
fi

# Check if Docker is configured for Artifact Registry
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | head -n1 | grep -q "@"; then
    echo -e "${YELLOW}⚠️  Configuring Docker for Artifact Registry...${NC}"
    gcloud auth configure-docker "${REGISTRY_URL}" --quiet
fi

echo -e "${GREEN}✅ All prerequisites validated successfully${NC}"
echo ""

# Docker Build Process
echo -e "${BLUE}🔨 Building Docker image...${NC}"
echo -e "${BLUE}   Building: ${DOCKER_IMAGE_NAME}:${IMAGE_TAG}${NC}"

if docker build -t "${DOCKER_IMAGE_NAME}:${IMAGE_TAG}" .; then
    echo -e "${GREEN}✅ Docker build completed successfully${NC}"
else
    echo -e "${RED}❌ Docker build failed${NC}"
    exit 1
fi

# Image Tagging for Artifact Registry
echo -e "${BLUE}🏷️  Tagging image for Artifact Registry...${NC}"
echo -e "${BLUE}   Tagging as: ${FULL_IMAGE_URL}${NC}"

if docker tag "${DOCKER_IMAGE_NAME}:${IMAGE_TAG}" "${FULL_IMAGE_URL}"; then
    echo -e "${GREEN}✅ Image tagged successfully${NC}"
else
    echo -e "${RED}❌ Image tagging failed${NC}"
    exit 1
fi

# Push to Artifact Registry
echo -e "${BLUE}📤 Pushing image to Artifact Registry...${NC}"
echo -e "${BLUE}   Pushing to: ${FULL_IMAGE_URL}${NC}"

if docker push "${FULL_IMAGE_URL}"; then
    echo -e "${GREEN}✅ Image pushed successfully to Artifact Registry${NC}"
else
    echo -e "${RED}❌ Image push failed${NC}"
    exit 1
fi

# Deployment Success Summary
echo ""
echo -e "${GREEN}🎉 Deployment completed successfully!${NC}"
echo -e "${GREEN}============================================================================${NC}"
echo -e "${GREEN}📦 Image Details:${NC}"
echo -e "   • Local Image: ${DOCKER_IMAGE_NAME}:${IMAGE_TAG}"
echo -e "   • Registry URL: ${FULL_IMAGE_URL}"
echo -e "   • Project: ${GCP_PROJECT_ID}"
echo -e "   • Region: ${GCP_REGION}"
echo -e "   • Registry: ${ARTIFACT_REGISTRY}"
echo ""
echo -e "${BLUE}💡 Next Steps:${NC}"
echo -e "   • Deploy to Cloud Run: gcloud run deploy"
echo -e "   • Use in Kubernetes: kubectl apply -f deployment.yaml"
echo -e "   • Set up CI/CD: Configure GitHub Actions or Cloud Build"
echo ""
echo -e "${YELLOW}📝 Note: This script is for local deployment. Use CI/CD for production.${NC}"
