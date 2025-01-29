#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Step 1: Create a Python virtual environment
echo "Creating Python virtual environment..."
python -m venv .venv

# Step 2: Activate the virtual environment
echo "Activating virtual environment..."
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    # Linux or macOS
    source .venv/bin/activate
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
    # Windows (MSYS, Cygwin, or native)
    source .venv/Scripts/activate
else
    echo "Unsupported platform: $OSTYPE"
    exit 1
fi

# Step 3: Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete. Virtual environment is ready."
