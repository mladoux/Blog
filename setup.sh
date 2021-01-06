#!/bin/bash

# Create environment
python3 -m venv venv

# Activate environment
source venv/bin/activate

# Install dependencies
pip install pip --upgrade
pip install $(cat requirements.txt)

# Generate app secret
SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')

# add app secret to environment config
echo "SECRET_KEY=$SECRET_KEY" > app/.env

# Notify user
echo "Initial setup complete!"
echo "Run \`source venv/bin/activate\` to enter virtual environment!"
