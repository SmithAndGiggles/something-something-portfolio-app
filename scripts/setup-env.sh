#!/bin/bash

# ================================================================# Development environment ready!
echo ""
echo "🎉 Virtual environment setup complete!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🔧 DEVELOPMENT WORKFLOW:"
echo ""
echo "1️⃣  Activate virtual environment:"
echo "   source $VENV_DIR/bin/activate"
echo ""
echo "2️⃣  Run Flask development server:"
echo "   python main.py"
echo "   OR directly: $VENV_DIR/bin/python main.py"
echo ""
echo "3️⃣  Access your portfolio:"
echo "   🌐 http://localhost:8080"
echo ""
echo "4️⃣  Deactivate when done:"
echo "   deactivate"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🤖 Starting development server automatically..."
echo ""

# Auto-start the Flask development server
"$VENV_DIR/bin/python" main.py# Flask Portfolio Development Environment Setup Script
# ==============================================================================
#
# Purpose: Automated setup of Python virtual environment for Flask portfolio app
# Location: scripts/setup-env.sh (run from project root directory)
# Usage: ./scripts/setup-env.sh
#
# Features:
# - Clean virtual environment creation with dependency management
# - Automatic package installation from pyproject.toml
# - Flask installation verification
# - Development server auto-start
# - Clear usage instructions for development workflow
#
# Requirements:
# - Python 3.8+ installed and available as 'python3'
# - Project pyproject.toml file in root directory
# - Execute from project root directory (not from scripts/)
#
# ==============================================================================

# Configuration
VENV_DIR="me2u-venv-flask"
PROJECT_ROOT="$(pwd)"

# Verify we're in the correct directory (should contain pyproject.toml)
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found in current directory"
    echo "💡 Please run this script from the project root directory:"
    echo "   ./scripts/setup-env.sh"
    exit 1
fi

echo "🚀 Setting up Flask development environment..."
echo "📁 Project root: $PROJECT_ROOT"
echo "🐍 Virtual environment: $VENV_DIR"
echo ""

# Clean slate: Remove any existing virtual environment
if [ -d "$VENV_DIR" ]; then
    echo "🔄 Removing existing virtual environment..."
    rm -rf "$VENV_DIR"
fi

# Create fresh virtual environment
echo "🚧 Creating new virtual environment: $VENV_DIR"
python3 -m venv "$VENV_DIR"

# Check if virtual environment was created successfully
if [ ! -d "$VENV_DIR" ]; then
    echo "❌ Failed to create virtual environment"
    echo "💡 Please ensure Python 3.8+ is installed: python3 --version"
    exit 1
fi

# Upgrade pip for latest dependency resolution
echo "⬆️  Upgrading pip to latest version..."
"$VENV_DIR/bin/pip" install --upgrade pip

# Install project dependencies from pyproject.toml in development mode
echo "📦 Installing project dependencies from pyproject.toml..."
"$VENV_DIR/bin/pip" install -e .

# Install additional development dependencies
echo "🔧 Installing additional development tools..."
"$VENV_DIR/bin/pip" install toml

# Verify critical dependencies are installed
echo "✅ Verifying Flask installation..."
if "$VENV_DIR/bin/python" -c "import flask; print('✅ Flask', flask.__version__, 'installed successfully')" 2>/dev/null; then
    echo "✅ Flask is ready for development"
else
    echo "❌ Flask installation verification failed"
    exit 1
fi

# Show how to use the environment
echo "✅ Virtual environment setup complete!"
echo "� To activate it, run:"
echo "   source $VENV_DIR/bin/activate"
echo ""
echo "🚀 To run your Flask app:"
echo "   $VENV_DIR/bin/python main.py"
echo "   OR activate first: source $VENV_DIR/bin/activate && python main.py"
echo ""
echo "🌐 Your app will be available at: http://localhost:8080"
echo ""
echo "🤖 Running app automatically..."

# Run the app directly using the venv's Python (fully automated)
"$VENV_DIR/bin/python" main.py