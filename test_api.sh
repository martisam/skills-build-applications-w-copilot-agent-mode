#!/bin/bash

# API Testing Script for OctoFit Tracker
# This script tests the API endpoints using curl

# Get the base URL
if [ -z "$CODESPACE_NAME" ]; then
    BASE_URL="http://localhost:8000"
    echo "Using localhost: $BASE_URL"
else
    BASE_URL="https://$CODESPACE_NAME-8000.app.github.dev"
    echo "Using Codespace: $BASE_URL"
fi

echo "================================================"
echo "OctoFit Tracker API Testing"
echo "================================================"
echo ""

# Test 1: API Root Endpoint
echo "Test 1: API Root Endpoint"
echo "URL: $BASE_URL/"
echo "---"
curl -s -k "$BASE_URL/" | python3 -m json.tool || curl -s "$BASE_URL/"
echo ""
echo ""

# Test 2: Users Endpoint
echo "Test 2: Users Endpoint"
echo "URL: $BASE_URL/api/users/"
echo "---"
curl -s -k "$BASE_URL/api/users/" | python3 -m json.tool || curl -s "$BASE_URL/api/users/"
echo ""
echo ""

# Test 3: Activities Endpoint
echo "Test 3: Activities Endpoint"
echo "URL: $BASE_URL/api/activities/"
echo "---"
curl -s -k "$BASE_URL/api/activities/" | python3 -m json.tool || curl -s "$BASE_URL/api/activities/"
echo ""
echo ""

# Test 4: Teams Endpoint
echo "Test 4: Teams Endpoint"
echo "URL: $BASE_URL/api/teams/"
echo "---"
curl -s -k "$BASE_URL/api/teams/" | python3 -m json.tool || curl -s "$BASE_URL/api/teams/"
echo ""
echo ""

# Test 5: Workouts Endpoint
echo "Test 5: Workouts Endpoint"
echo "URL: $BASE_URL/api/workouts/"
echo "---"
curl -s -k "$BASE_URL/api/workouts/" | python3 -m json.tool || curl -s "$BASE_URL/api/workouts/"
echo ""
echo ""

echo "================================================"
echo "Testing Complete"
echo "================================================"
