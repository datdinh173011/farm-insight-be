#!/usr/bin/env bash
set -euo pipefail

# Resolve project root (one level up from scripts/)
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

# Activate virtualenv and apply migrations
source "$PROJECT_ROOT/venv/bin/activate"
pip install -r requirements.txt
python manage.py migrate

# Reload services
sudo systemctl daemon-reload
sudo systemctl restart farm-insight
sudo nginx -t && sudo systemctl reload nginx
