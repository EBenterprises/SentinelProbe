#!/bin/bash
# Push automation for SentinelProbe

# 1. Initialize Git
git init

# 2. Add files
git add .

# 3. Initial commit
git commit -m "Initial commit: SentinelProbe Framework"

# 4. Authenticate and create repo (Requires prior 'gh auth login')
# Replace 'YOUR_USERNAME' with your actual GitHub username
REPO_NAME="SentinelProbe"
gh repo create $REPO_NAME --public --source=. --remote=origin --push

echo "Successfully pushed to GitHub!"
