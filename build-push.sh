#!/bin/sh
# Usage: ./build-push.sh <image-name> <tag>
# Example: ./build-push.sh myapp v1

set -e

# Google Cloud Artifact Registry Configuration
LOCATION="us-central1"
PROJECT_ID="me2u-prj-app-prod-3aa8"
REGISTRY_NAME="me2u-artifact-docker"
REGISTRY_BASE="docker.pkg.dev"

# Image Configuration
IMAGE_NAME=${1:-me2u}
TAG=${2:-latest}

# Build full repository URL
REPO="$LOCATION-$REGISTRY_BASE/$PROJECT_ID/$REGISTRY_NAME"
FULL_IMAGE="$REPO/$IMAGE_NAME:$TAG"
LOCAL_IMAGE="$IMAGE_NAME:$TAG"

echo "🔨 Building Docker image: $LOCAL_IMAGE"
docker build -t "$LOCAL_IMAGE" .

echo "🏷️  Tagging image for Google Cloud Artifact Registry: $FULL_IMAGE"
docker tag "$LOCAL_IMAGE" "$FULL_IMAGE"

echo "🚀 Pushing Docker image to Google Cloud: $FULL_IMAGE"
docker push "$FULL_IMAGE"

echo "✅ Done. Image pushed: $FULL_IMAGE"
echo "📍 Location: $LOCATION"
echo "🏗️  Project: $PROJECT_ID"
echo "📦 Registry: $REGISTRY_NAME"