#!/bin/bash

# ------------------------------------------------------------------------------
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

# Install dependencies from requirements.txt
echo "📦 Installing dependencies from requirements.txt..."
"$VENV_DIR/bin/pip" install -r requirements.txt

# Confirm Flask is properly installed
echo "✅ Verifying Flask installation..."
"$VENV_DIR/bin/python" -c "import flask; print('✅ Flask is installed and available.')"

# Final instructions
echo "✅ Virtual environment setup complete!"
echo "🚀 Starting Flask app automatically..."
echo "🌐 Your app will be available at: http://localhost:8080"
echo ""

# Run the app directly using the venv's Python (fully automated)
"$VENV_DIR/bin/python" main.py