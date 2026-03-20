#!/bin/bash

# Script to create ansible-samba project structure

set -e

BASE_DIR="ansible-samba"

echo "Creating ansible-samba project structure..."

# Create directories
mkdir -p "$BASE_DIR/group_vars"
mkdir -p "$BASE_DIR/roles/samba_repo/tasks"
mkdir -p "$BASE_DIR/roles/samba_repo/templates"
mkdir -p "$BASE_DIR/roles/samba_repo/handlers"

# Create files
touch "$BASE_DIR/inventory"
touch "$BASE_DIR/playbook.yml"
touch "$BASE_DIR/group_vars/all.yml"
touch "$BASE_DIR/roles/samba_repo/tasks/main.yml"
touch "$BASE_DIR/roles/samba_repo/templates/smb.conf.j2"
touch "$BASE_DIR/roles/samba_repo/handlers/main.yml"

echo "Done! Folder structure created:"
echo ""
find "$BASE_DIR" | sort | sed 's|[^/]*/|  |g; s|  \([^ ]\)|└── \1|'

