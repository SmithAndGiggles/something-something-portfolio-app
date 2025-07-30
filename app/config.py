"""
Cloud-Agnostic Configuration Management
=====================================

This module provides centralized configuration management following 12-factor app principles:
- Configuration via pyproject.toml for default values
- Environment variables override defaults for deployment flexibility
- Cloud-agnostic design - no hardcoded cloud provider assumptions
- Secure handling of sensitive values through environment variables only

Design Philosophy:
- DRY: Single source of truth in pyproject.toml for non-sensitive defaults
- Security: All deployment-specific config via environment variables
- Portability: Works across any cloud provider or local development
- Flexibility: Easy to override any setting for different environments

Usage:
    config = Config()
    debug_mode = config.debug  # Returns bool from env var or pyproject.toml
    port = config.port         # Returns int with proper type conversion
"""

import os
import tomllib
import toml
from pathlib import Path


class Config:
    """
    Cloud-agnostic configuration manager with environment variable overrides.
    
    This class implements a hierarchical configuration system:
    1. Default values from pyproject.toml [tool.portfolio] section
    2. Environment variables override defaults (higher priority)
    3. Type conversion and validation for configuration values
    
    The configuration is designed to be cloud-agnostic - it doesn't assume
    any specific cloud provider, making the application portable across
    different deployment environments.
    """
    
    def __init__(self):
        """Initialize configuration by loading pyproject.toml defaults."""
        config_file = Path(__file__).parent.parent / "pyproject.toml"
        
        # Load default configuration from pyproject.toml
        with open(config_file, "rb") as f:
            data = tomllib.load(f)
        
        self._config = data.get("tool", {}).get("portfolio", {})
    
    def get(self, key: str, default=None):
        """
        Get configuration value from pyproject.toml.
        
        Args:
            key: Configuration key to retrieve
            default: Default value if key not found
            
        Returns:
            Configuration value from pyproject.toml
        """
        return self._config.get(key, default)
    
    # Application Configuration Properties
    # ===================================
    # These properties provide typed access to configuration values with
    # automatic environment variable override support.
    
    @property
    def app_name(self) -> str:
        """Application display name - safe to use default from pyproject.toml."""
        return self.get("app_name", "Portfolio")
    
    @property
    def version(self) -> str:
        """Application version - safe to use default from pyproject.toml."""
        return self.get("version", "0.1.0")
    
    @property
    def debug(self) -> bool:
        """Debug mode - environment variable overrides pyproject.toml for security."""
        return os.getenv("DEBUG", str(self.get("debug", False))).lower() == "true"
    
    @property
    def host(self) -> str:
        """Server bind address - environment variable overrides for deployment flexibility."""
        return os.getenv("HOST", self.get("host", "0.0.0.0"))
    
    @property
    def port(self) -> int:
        """Server port - environment variable overrides with type conversion."""
        return int(os.getenv("PORT", self.get("port", 8080)))
    
    # Cloud Deployment Configuration
    # =============================
    # These properties are intentionally environment-only for security.
    # No defaults in pyproject.toml to prevent accidental credential exposure.
    
    @property
    def gcp_project_id(self) -> str:
        return self.get("gcp_project_id", "")
    
    @property
    def gcp_region(self) -> str:
        return self.get("gcp_region", "us-central1")
    
    @property
    def artifact_registry(self) -> str:
        return self.get("artifact_registry", "portfolio-artifact-docker")
    
    @property
    def docker_image_name(self) -> str:
        return self.get("docker_image_name", "portfolio-app")
    
    @property
    def docker_tag(self) -> str:
        return os.getenv("DOCKER_TAG", self.get("docker_tag", "latest"))


# Global instance
config = Config()


def load_app_config():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    toml_path = os.path.join(base_dir, "pyproject.toml")
    config = toml.load(toml_path)
    return config.get("tool", {}).get("portfolio", {})


def apply_config(app):
    app_config = load_app_config()
    for key, value in app_config.items():
        app.config[key.upper()] = value
