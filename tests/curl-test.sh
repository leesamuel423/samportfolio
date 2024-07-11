#!/bin/bash
# Author: leesamuel423

BASE_URL="http://localhost:5001/api/timeline_post"

# Generate random string
random_string() {
  LC_ALL=C tr -dc 'A-Za-z0-9' < /dev/urandom | head -c $1
}

# Random Data for Timeline Post
NAME=$(random_string 10)
EMAIL="$NAME@gmail.com"
CONTENT=$(random_string 50)

echo "name: $NAME"
echo "email: $EMAIL"
echo "content: $CONTENT"

# POST Endpoint Testing
echo "Testing POST endpoints..."
P_RESPONSE=$(curl -s --request POST "${BASE_URL}" -d "name=${NAME}&email=${EMAIL}&content=${CONTENT}")

echo "POST Response: $P_RESPONSE"

if [[ $P_RESPONSE == *"id"* ]]; then
  echo "POST test passed: Timeline post created successfully"
  POST_ID=$(echo $P_RESPONSE | sed 's/.*"id":\([0-9]*\).*/\1/')
else
  echo "POST test failed: Unable to create timeline post\n"
  exit 1
fi


# GET Endpoint Testing
echo "Testing GET endpoints..."
G_RESPONSE=$(curl -s "${BASE_URL}")

if [[ $G_RESPONSE == *"$CONTENT"* ]]; then
  echo "GET test passed: Timeline posts retrieved successfully"
else
  echo "GET test failed: Unable to retrieve timeline posts"
  exit 1
fi


# DELETE Endpoint Testing
echo "Testing DELETE endpoints..."
D_RESPONSE=$(curl -s --request DELETE "${BASE_URL}/${POST_ID}")

if [[ $D_RESPONSE == *"\"deleted\":true"* ]]; then
  echo "DELETE test passed: Timeline post deleted successfully"
else
  echo "DELETE test failed: Unable to delete timeline post"
  exit 1
fi

# Verify deleted
FINAL_G_RESPONSE=$(curl -s "${BASE_URL}")

if [[ $G_RESPONSE != *"\"id\": ${POST_ID}"* ]]; then
  echo "Final GET test passed: Timeline posts in original state"
else
  echo "Final GET test failed: Timeline posts not in original state"
  exit 1
fi

echo "All tests completed successfully!"



