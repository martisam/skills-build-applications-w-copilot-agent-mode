@echo off
REM API Testing Script for OctoFit Tracker (Windows)
REM This script tests the API endpoints using curl

setlocal enabledelayedexpansion

REM Get the base URL
if defined CODESPACE_NAME (
    set "BASE_URL=https://%CODESPACE_NAME%-8000.app.github.dev"
    echo Using Codespace: !BASE_URL!
) else (
    set "BASE_URL=http://localhost:8000"
    echo Using localhost: !BASE_URL!
)

echo ================================================
echo OctoFit Tracker API Testing
echo ================================================
echo.

REM Test 1: API Root Endpoint
echo Test 1: API Root Endpoint
echo URL: !BASE_URL!/
echo ---
curl -s -k "!BASE_URL!/"
echo.
echo.

REM Test 2: Users Endpoint
echo Test 2: Users Endpoint
echo URL: !BASE_URL!/api/users/
echo ---
curl -s -k "!BASE_URL!/api/users/"
echo.
echo.

REM Test 3: Activities Endpoint
echo Test 3: Activities Endpoint
echo URL: !BASE_URL!/api/activities/
echo ---
curl -s -k "!BASE_URL!/api/activities/"
echo.
echo.

REM Test 4: Teams Endpoint
echo Test 4: Teams Endpoint
echo URL: !BASE_URL!/api/teams/
echo ---
curl -s -k "!BASE_URL!/api/teams/"
echo.
echo.

REM Test 5: Workouts Endpoint
echo Test 5: Workouts Endpoint
echo URL: !BASE_URL!/api/workouts/
echo ---
curl -s -k "!BASE_URL!/api/workouts/"
echo.
echo.

echo ================================================
echo Testing Complete
echo ================================================
