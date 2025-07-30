# ================================================================
# Portfolio App - Script Configuration
# ================================================================
# This file contains all configurable variables for deployment scripts
# Source this file in scripts: source scripts/config.sh

# ================================================================
# Application Configuration
# ================================================================
export APP_NAME="me2u Portfolio"
export APP_VERSION="1.0.0"
export DOCKER_IMAGE_NAME="portfolio-app"
export DEFAULT_IMAGE_TAG="latest"

# ================================================================
# Development Environment
# ================================================================
export DEV_VENV_DIR="me2u-venv-flask"
export DEV_PORT="8080"
export DEV_HOST="localhost"

# ================================================================
# GCP Configuration Templates (override via environment)
# ================================================================
export DEFAULT_GCP_REGION="us-central1"
export DEFAULT_ARTIFACT_REGISTRY="portfolio-registry"

# ================================================================
# Script Behavior
# ================================================================
export SCRIPT_COLORS_ENABLED="true"
export SCRIPT_VERBOSE="false"
export SCRIPT_AUTO_START="true"

# ================================================================
# Validation Rules
# ================================================================
export REQUIRED_GCP_VARS="GCP_PROJECT_ID GCP_REGION ARTIFACT_REGISTRY"
export REQUIRED_PYTHON_VERSION="3.8"

# ================================================================
# Helper Functions
# ================================================================

# Load environment-specific overrides
load_env_overrides() {
    local env_file="${1:-.env}"
    if [[ -f "$env_file" ]]; then
        echo "📁 Loading overrides from $env_file..."
        set -a  # automatically export all variables
        source "$env_file"
        set +a
    fi
}

# Get value with fallback priority: ENV_VAR -> pyproject.toml -> default
get_config_value() {
    local var_name="$1"
    local toml_key="$2" 
    local default_value="$3"
    
    # 1. Check environment variable
    if [[ -n "${!var_name:-}" ]]; then
        echo "${!var_name}"
        return
    fi
    
    # 2. Check pyproject.toml
    if [[ -n "$toml_key" ]] && command -v python3 &> /dev/null; then
        local toml_value
        toml_value=$(python3 -c "
import tomllib
try:
    with open('pyproject.toml', 'rb') as f:
        data = tomllib.load(f)
    value = data.get('tool', {}).get('me2u', {}).get('$toml_key', '')
    print(value) if value else exit(1)
except Exception:
    exit(1)
" 2>/dev/null)
        if [[ -n "$toml_value" ]]; then
            echo "$toml_value"
            return
        fi
    fi
    
    # 3. Use default
    echo "$default_value"
}

# Validate required variables with helpful messages
validate_required_vars() {
    local required_vars="$1"
    local missing_vars=()
    
    for var in $required_vars; do
        if [[ -z "${!var:-}" ]]; then
            missing_vars+=("$var")
        fi
    done
    
    if [[ ${#missing_vars[@]} -gt 0 ]]; then
        echo "❌ Missing required variables: ${missing_vars[*]}"
        echo "💡 Set in .env file or export directly"
        return 1
    fi
    
    return 0
}
