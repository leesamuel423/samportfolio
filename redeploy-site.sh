#!/bin/bash
# Author: leesamuel423


# Step 1: Change to project directory
cd samportfolio || exit

# Step 2: Fetch and reset the git repository to the latest changes from the main branch
git fetch && git reset origin/main --hard

# Step 3: Enter the python virtual environment and install python dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Step 4: Restart myportfolio service
sudo systemctl restart myportfolio

# Step 5: Check status of service
sudo systemctl status myportfolio
