"""
Simple configuration module for me2u portfolio application.
Reads from pyproject.toml for DRY principles.
"""

import os
import tomllib
import toml
from pathlib import Path


class Config:
    """Simple configuration class that reads from pyproject.toml"""
    
    def __init__(self):
        config_file = Path(__file__).parent.parent / "pyproject.toml"
        
        with open(config_file, "rb") as f:
            data = tomllib.load(f)
        
        self._config = data.get("tool", {}).get("me2u", {})
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        return self._config.get(key, default)
    
    # App settings
    @property
    def app_name(self) -> str:
        return self.get("app_name", "me2u Portfolio")
    
    @property
    def version(self) -> str:
        return self.get("version", "0.1.0")
    
    @property
    def debug(self) -> bool:
        return os.getenv("DEBUG", str(self.get("debug", False))).lower() == "true"
    
    @property
    def host(self) -> str:
        return os.getenv("HOST", self.get("host", "0.0.0.0"))
    
    @property
    def port(self) -> int:
        return int(os.getenv("PORT", self.get("port", 8080)))
    
    # Docker/GCP settings
    @property
    def gcp_project_id(self) -> str:
        return self.get("gcp_project_id", "")
    
    @property
    def gcp_region(self) -> str:
        return self.get("gcp_region", "us-central1")
    
    @property
    def artifact_registry(self) -> str:
        return self.get("artifact_registry", "me2u-artifact-docker")
    
    @property
    def docker_image_name(self) -> str:
        return self.get("docker_image_name", "me2u")
    
    @property
    def docker_tag(self) -> str:
        return os.getenv("DOCKER_TAG", self.get("docker_tag", "latest"))


# Global instance
config = Config()


def load_app_config():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    toml_path = os.path.join(base_dir, "pyproject.toml")
    config = toml.load(toml_path)
    return config.get("tool", {}).get("me2u", {})


def apply_config(app):
    app_config = load_app_config()
    for key, value in app_config.items():
        app.config[key.upper()] = value
