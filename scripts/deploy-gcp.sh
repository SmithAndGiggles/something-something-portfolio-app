#!/bin/bash

# ============================================================================
# GCP Deployment Script - Refactored with Best Practices
# ============================================================================

set -e  # Exit on error

# ================================================================
# Configuration Loading
# ================================================================

# Get script directory for relative imports
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Load shared configuration
source "$SCRIPT_DIR/config.sh"

# Load environment-specific overrides
ENVIRONMENT="${ENVIRONMENT:-development}"
load_env_overrides "$SCRIPT_DIR/.env.$ENVIRONMENT"
load_env_overrides "$PROJECT_ROOT/.env"  # Project root .env has highest priority

# ================================================================
# Variable Resolution with Priority System
# ================================================================

# Resolve all configuration with priority: ENV -> pyproject.toml -> defaults
APP_NAME=$(get_config_value "APP_NAME" "app_name" "$APP_NAME")
APP_VERSION="${APP_VERSION:-0.0.0}"  # Default to "0.0.0" if not set
VERSION=$(get_config_value "VERSION" "version" "$APP_VERSION")  
DOCKER_IMAGE_NAME=$(get_config_value "DOCKER_IMAGE_NAME" "container_image_name" "$DOCKER_IMAGE_NAME")
IMAGE_TAG=$(get_config_value "IMAGE_TAG" "container_tag" "$DEFAULT_IMAGE_TAG")

# GCP Configuration (environment only for security)
GCP_PROJECT_ID="${GCP_PROJECT_ID}"
GCP_REGION="${GCP_REGION:-$DEFAULT_GCP_REGION}"
ARTIFACT_REGISTRY="${ARTIFACT_REGISTRY:-$DEFAULT_ARTIFACT_REGISTRY}"

# ================================================================
# Script Execution
# ================================================================

# Load colors if enabled
if [[ "$SCRIPT_COLORS_ENABLED" == "true" ]]; then
    source "$SCRIPT_DIR/colors.sh"
else
    # Define empty color variables
    RED="" GREEN="" YELLOW="" BLUE="" PURPLE="" NC=""
fi

echo -e "${BLUE}🚀 GCP Deployment Script${NC}"
echo -e "${BLUE}Environment: $ENVIRONMENT${NC}"
echo ""

# Display configuration
echo -e "${PURPLE}📋 Configuration:${NC}"
echo -e "   • App: $APP_NAME v$VERSION"
echo -e "   • Image: $DOCKER_IMAGE_NAME:$IMAGE_TAG"
echo -e "   • Project: ${GCP_PROJECT_ID:-'<not set>'}"
echo -e "   • Region: $GCP_REGION"
echo ""

# Validate required variables
if ! validate_required_vars "$REQUIRED_GCP_VARS"; then
    exit 1
fi

# Derived Configuration
REGISTRY_URL="${GCP_REGION}-docker.pkg.dev"
FULL_IMAGE_URL="${REGISTRY_URL}/${GCP_PROJECT_ID}/${ARTIFACT_REGISTRY}/${DOCKER_IMAGE_NAME}:${IMAGE_TAG}"

print_success "Configuration validated"

# ================================================================
# Docker and GCP Validation
# ================================================================

print_info "Validating prerequisites..."

# Validate Docker
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed or not in PATH"
    echo "💡 Install Docker: https://docs.docker.com/get-docker/"
    exit 1
fi

if ! docker info &> /dev/null; then
    print_error "Docker daemon is not running"
    echo "💡 Start Docker and try again"
    exit 1
fi

# Validate Google Cloud CLI
if ! command -v gcloud &> /dev/null; then
    print_error "Google Cloud CLI (gcloud) is not installed"
    echo "💡 Install gcloud: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Check authentication
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | head -n1 | grep -q "@"; then
    print_error "Not authenticated to Google Cloud"
    echo "💡 Run: gcloud auth login"
    exit 1
fi

# Configure Docker for Artifact Registry
print_info "Configuring Docker for Artifact Registry..."
gcloud auth configure-docker "${REGISTRY_URL}" --quiet

print_success "All prerequisites validated"

# ================================================================
# Docker Build and Deploy
# ================================================================

print_info "Building Docker image: ${DOCKER_IMAGE_NAME}:${IMAGE_TAG}"

if docker build -t "${DOCKER_IMAGE_NAME}:${IMAGE_TAG}" .; then
    print_success "Docker build completed"
else
    print_error "Docker build failed"
    exit 1
fi

print_info "Tagging image for Artifact Registry: ${FULL_IMAGE_URL}"

if docker tag "${DOCKER_IMAGE_NAME}:${IMAGE_TAG}" "${FULL_IMAGE_URL}"; then
    print_success "Image tagged successfully"
else
    print_error "Image tagging failed"
    exit 1
fi

print_info "Pushing image to Artifact Registry..."

if docker push "${FULL_IMAGE_URL}"; then
    print_success "Image pushed successfully to Artifact Registry"
else
    print_error "Image push failed"
    exit 1
fi

# ================================================================
# Success Summary
# ================================================================

echo ""
print_success "Deployment completed successfully!"
echo ""
print_highlight "Image Details:"
echo "   • Local Image: ${DOCKER_IMAGE_NAME}:${IMAGE_TAG}"
echo "   • Registry URL: ${FULL_IMAGE_URL}"
echo "   • Project: ${GCP_PROJECT_ID}"
echo "   • Region: ${GCP_REGION}"
echo ""
print_info "Next Steps:"
echo "   • Deploy to Cloud Run: gcloud run deploy"
echo "   • Use in Kubernetes: kubectl apply -f deployment.yaml"
echo "   • Set up CI/CD: Configure GitHub Actions or Cloud Build"
