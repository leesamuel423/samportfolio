#!/bin/bash
# Author: leesamuel423


# Step 1: Change to project directory
cd samportfolio || exit

# Step 2: Fetch and reset the git repository to the latest changes from the main branch
git fetch && git reset origin/main --hard

# Step 3: Spin down existing containers
docker compose -f docker-compose.prod.yml down

# Step 4: Build and start containers
docker compose -f docker-compose.prod.yml up -d --build

# Step 5: Check status of containers
docker ps
