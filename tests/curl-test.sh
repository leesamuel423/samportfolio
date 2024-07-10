#!/usr/env bash
# Author: leesamuel423

BASE_URL="http//localhost:5001/api"

# Generate random string
random_string() {
  cat /dev/urandom | head -n 1
}

# Random Data for Timeline Post
NAME=$(random_string)
EMAIL="$NAME@gmail.com"
CONTENT=$(random_string)

echo "name: $NAME"
echo "email: $EMAIL"
echo "content: $CONTENT"

# POST Endpoint Testing
echo "Testing POST endpoints..."
