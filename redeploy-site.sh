#!/bin/bash
# Author: leesamuel423

# Step 1: Kill all existing tmux sessions
tmux kill-server

# Step 2: Change to project directory
cd samportfolio || exit

# Step 3: Fetch and reset the git repository to the latest changes from the main branch
git fetch && git reset origin/main --hard

# Step 4: Enter the python virtual environment and install python dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Step 5: Start a new detached tmux session that starts the Flask server
tmux new -s portfolio "source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"
