#!/bin/bash

# Create environment
python3 -m venv venv

# Activate environment
source venv/bin/activate

# Install dependencies
pip install pip --upgrade
pip install $(cat requirements.txt)

echo "Dependencies installed!"
echo "Run \`source venv/bin/activate\` to enter virtual environment!"
