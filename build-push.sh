#!/bin/bash

# ============================================================================
# me2u - Dynamic Docker Build & Push Script
# Reads configuration from pyproject.toml for DRY principles
# ============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper function to extract values from pyproject.toml
get_toml_value() {
    local key="$1"
    local default="$2"
    
    if command -v python3 &> /dev/null; then
        python3 -c "
import tomllib
import sys
try:
    with open('pyproject.toml', 'rb') as f:
        data = tomllib.load(f)
    value = data.get('tool', {}).get('me2u', {}).get('$key', '$default')
    print(value)
except Exception as e:
    print('$default')
"
    else
        echo "$default"
    fi
}

# Load configuration from pyproject.toml
echo -e "${BLUE}📖 Loading configuration from pyproject.toml...${NC}"

APP_NAME=$(get_toml_value "app_name" "me2u Portfolio")
VERSION=$(get_toml_value "version" "0.1.0")
GCP_PROJECT_ID=${GCP_PROJECT_ID:-$(get_toml_value "gcp_project_id" "default-gcp-project-id")}
GCP_REGION=$(get_toml_value "gcp_region" "us-central1")
ARTIFACT_REGISTRY=$(get_toml_value "artifact_registry" "me2u-artifact-docker")
DOCKER_REGISTRY_BASE=$(get_toml_value "docker_registry_base" "docker.pkg.dev")
DOCKER_IMAGE_NAME=$(get_toml_value "docker_image_name" "me2u")
DOCKER_TAG=$(get_toml_value "docker_tag" "latest")

# Allow command line overrides
IMAGE_NAME=${1:-$DOCKER_IMAGE_NAME}
TAG=${2:-$DOCKER_TAG}

# Build full repository URL
REPO="$GCP_REGION-$DOCKER_REGISTRY_BASE/$GCP_PROJECT_ID/$ARTIFACT_REGISTRY"
FULL_IMAGE="$REPO/$IMAGE_NAME:$TAG"
LOCAL_IMAGE="$IMAGE_NAME:$TAG"

# Display configuration
echo -e "${GREEN}✅ Configuration loaded:${NC}"
echo -e "  📱 App Name: $APP_NAME"
echo -e "  🔢 Version: $VERSION"
echo -e "  🏗️  Project: $GCP_PROJECT_ID"
echo -e "  📍 Region: $GCP_REGION"
echo -e "  📦 Registry: $ARTIFACT_REGISTRY"
echo -e "  🐳 Image: $IMAGE_NAME:$TAG"
echo -e "  🌐 Full URL: $FULL_IMAGE"
echo ""

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo -e "${RED}❌ Docker is not running. Please start Docker and try again.${NC}"
    exit 1
fi

# Build Docker image
echo -e "${YELLOW}🔨 Building Docker image: $LOCAL_IMAGE${NC}"
docker build \
    --build-arg APP_NAME="$APP_NAME" \
    --build-arg VERSION="$VERSION" \
    --tag "$LOCAL_IMAGE" \
    .

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Docker build successful${NC}"
else
    echo -e "${RED}❌ Docker build failed${NC}"
    exit 1
fi

# Tag image for Google Cloud Artifact Registry
echo -e "${YELLOW}🏷️  Tagging image for Google Cloud Artifact Registry: $FULL_IMAGE${NC}"
docker tag "$LOCAL_IMAGE" "$FULL_IMAGE"

# Push Docker image to Google Cloud
echo -e "${YELLOW}🚀 Pushing Docker image to Google Cloud: $FULL_IMAGE${NC}"
docker push "$FULL_IMAGE"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Docker push successful${NC}"
else
    echo -e "${RED}❌ Docker push failed${NC}"
    exit 1
fi

# Summary
echo ""
echo -e "${GREEN}🎉 Build and push completed successfully!${NC}"
echo -e "${GREEN}📍 Location: $GCP_REGION${NC}"
echo -e "${GREEN}🏗️  Project: $GCP_PROJECT_ID${NC}"
echo -e "${GREEN}📦 Registry: $ARTIFACT_REGISTRY${NC}"
echo -e "${GREEN}🐳 Image: $FULL_IMAGE${NC}"
echo ""
echo -e "${BLUE}💡 To deploy this image:${NC}"
echo -e "   gcloud run deploy me2u-app \\"
echo -e "     --image=$FULL_IMAGE \\"
echo -e "     --region=$GCP_REGION \\"
echo -e "     --project=$GCP_PROJECT_ID"