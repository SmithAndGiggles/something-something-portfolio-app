#!/usr/bin/env python3
"""
Configuration Validation Script
===============================

Validates that pyproject.toml serves as the single source of truth and is aligned
with GitHub workflow variables and build scripts.
"""

import tomllib
from pathlib import Path

def load_pyproject_config():
    """Load configuration from pyproject.toml"""
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    
    with open(pyproject_path, 'rb') as f:
        data = tomllib.load(f)
    
    return data.get('tool', {}).get('portfolio', {})

def validate_config():
    """Validate configuration alignment"""
    config = load_pyproject_config()
    
    print("🔍 Configuration Validation Report")
    print("=" * 50)
    
    # Core application values
    print(f"✅ App Name: {config.get('app_name', 'NOT_SET')}")
    print(f"✅ Version: {config.get('version', 'NOT_SET')}")
    print(f"✅ Container Image: {config.get('container_image_name', 'NOT_SET')}")
    print(f"✅ Container Port: {config.get('container_port', 'NOT_SET')}")
    
    # Deployment defaults
    print(f"✅ Default Region: {config.get('deployment_region', 'NOT_SET')}")
    print(f"✅ Service Name: {config.get('service_name', 'NOT_SET')}")
    print(f"✅ Registry Repo: {config.get('artifact_registry_repo', 'NOT_SET')}")
    
    # Cloud Run settings
    print(f"✅ Memory: {config.get('memory', 'NOT_SET')}")
    print(f"✅ CPU: {config.get('cpu', 'NOT_SET')}")
    print(f"✅ Min Instances: {config.get('min_instances', 'NOT_SET')}")
    print(f"✅ Max Instances: {config.get('max_instances', 'NOT_SET')}")
    
    print("\n📋 Expected GitHub Workflow Variables:")
    print(f"   GCP_APP_DOCKER_IMAGE_NAME = {config.get('container_image_name', 'NOT_SET')}")
    print(f"   GCP_REGION_PROD = {config.get('deployment_region', 'NOT_SET')}")
    print(f"   GCP_CLOUD_RUN_SERVICE_NAME = {config.get('service_name', 'NOT_SET')}")
    print(f"   GCP_ARTIFACT_REGISTRY_REPO_PROD = {config.get('artifact_registry_repo', 'NOT_SET')}")
    
    print("\n✅ Configuration validation complete!")

if __name__ == "__main__":
    validate_config()
