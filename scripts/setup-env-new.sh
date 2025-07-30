#!/bin/bash

# ================================================================
# Flask Development Environment Setup Script
# ================================================================
# Purpose: Automated setup of Python virtual environment for Flask portfolio app
# Usage: ./scripts/setup-env.sh

set -e  # Exit on error

# ================================================================
# Configuration Loading
# ================================================================

# Get script directory for relative imports
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Load shared configuration
source "$SCRIPT_DIR/config.sh"

# Load environment-specific overrides (development by default)
ENVIRONMENT="${ENVIRONMENT:-development}"
load_env_overrides "$SCRIPT_DIR/.env.$ENVIRONMENT"

# Load colors
if [[ "$SCRIPT_COLORS_ENABLED" == "true" ]]; then
    source "$SCRIPT_DIR/colors.sh"
else
    # Define empty color variables for compatibility
    RED="" GREEN="" YELLOW="" BLUE="" PURPLE="" NC=""
    print_error() { echo "❌ $1"; }
    print_success() { echo "✅ $1"; }
    print_warning() { echo "⚠️  $1"; }
    print_info() { echo "ℹ️  $1"; }
    print_highlight() { echo "🔸 $1"; }
fi

# ================================================================
# Setup Process
# ================================================================

print_info "Setting up Flask development environment..."
print_highlight "Project root: $PROJECT_ROOT"
print_highlight "Virtual environment: $DEV_VENV_DIR"
print_highlight "Environment: $ENVIRONMENT"
echo ""

# Verify we're in the correct directory
if [ ! -f "$PROJECT_ROOT/pyproject.toml" ]; then
    print_error "pyproject.toml not found in project root"
    echo "💡 Please run this script from the project root directory:"
    echo "   ./scripts/setup-env.sh"
    exit 1
fi

# Clean slate: Remove existing virtual environment
if [ -d "$PROJECT_ROOT/$DEV_VENV_DIR" ]; then
    print_info "Removing existing virtual environment..."
    rm -rf "$PROJECT_ROOT/$DEV_VENV_DIR"
fi

# Create fresh virtual environment
print_info "Creating virtual environment: $DEV_VENV_DIR"
cd "$PROJECT_ROOT"
python3 -m venv "$DEV_VENV_DIR"

# Check if virtual environment was created successfully
if [ ! -d "$DEV_VENV_DIR" ]; then
    print_error "Failed to create virtual environment"
    echo "💡 Please ensure Python 3.8+ is installed: python3 --version"
    exit 1
fi

# Upgrade pip
print_info "Upgrading pip to latest version..."
"$DEV_VENV_DIR/bin/pip" install --upgrade pip

# Install project dependencies
print_info "Installing project dependencies from pyproject.toml..."
"$DEV_VENV_DIR/bin/pip" install -e .

# Install development tools
print_info "Installing development tools..."
"$DEV_VENV_DIR/bin/pip" install toml

# Verify Flask installation
print_info "Verifying Flask installation..."
if "$DEV_VENV_DIR/bin/python" -c "import flask; print('✅ Flask', flask.__version__, 'installed successfully')" 2>/dev/null; then
    print_success "Flask is ready for development"
else
    print_error "Flask installation verification failed"
    exit 1
fi

# ================================================================
# Development Workflow Instructions
# ================================================================

echo ""
print_success "Virtual environment setup complete!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
print_highlight "DEVELOPMENT WORKFLOW:"
echo ""
echo "1️⃣  Activate virtual environment:"
echo "   source $DEV_VENV_DIR/bin/activate"
echo ""
echo "2️⃣  Run Flask development server:"
echo "   python main.py"
echo "   OR directly: $DEV_VENV_DIR/bin/python main.py"
echo ""
echo "3️⃣  Access your portfolio:"
echo "   🌐 http://$DEV_HOST:$DEV_PORT"
echo ""
echo "4️⃣  Deactivate when done:"
echo "   deactivate"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Auto-start server if enabled
if [[ "$SCRIPT_AUTO_START" == "true" ]]; then
    echo ""
    print_info "Starting development server automatically..."
    echo ""
    "$DEV_VENV_DIR/bin/python" main.py
else
    echo ""
    print_info "Setup complete! Run the server manually when ready."
fi
