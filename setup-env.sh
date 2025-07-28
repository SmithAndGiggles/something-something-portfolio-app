#!/bin/bash

# --------------# Show how to use the environment
echo "✅ Virtual environment setup complete!"
echo "👉 To activate it, run:"
echo "   source $VENV_DIR/bin/activate"
echo ""
echo "🚀 To run your Flask app:"
echo "   $VENV_DIR/bin/python main.py"
echo "   OR activate first: source $VENV_DIR/bin/activate && python main.py"
echo ""
echo "⚠️  NOTE: If you run 'py main.py' manually, first activate the venv:"
echo "   source $VENV_DIR/bin/activate"
echo "   Then: py main.py"
echo ""
echo "🌐 Your app will be available at: http://localhost:8080"
echo ""
echo "🤖 Running app automatically..."----------------------------------------------------
# me2u - Virtual Environment Setup Script for Flask App
# ------------------------------------------------------------------------------

# Define consistent virtual environment name
VENV_DIR="me2u-venv-flask"

# Remove any existing virtual environment
echo "🔄 Removing existing virtual environment (if any)..."
rm -rf "$VENV_DIR"

# Create a new virtual environment
echo "🚧 Creating new virtual environment: $VENV_DIR"
python3 -m venv "$VENV_DIR"

# Upgrade pip inside the venv
echo "⬆️  Upgrading pip..."
"$VENV_DIR/bin/pip" install --upgrade pip

# Install the package in development mode (reads pyproject.toml)
echo "📦 Installing package from pyproject.toml..."
"$VENV_DIR/bin/pip" install -e .

# Ensure toml is installed for config loading
source me2u-venv-flask/bin/activate
pip install --upgrade pip
pip install toml
deactivate

# Confirm Flask is properly installed
echo "✅ Verifying Flask installation..."
"$VENV_DIR/bin/python" -c "import flask; print('✅ Flask is installed and available.')"

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