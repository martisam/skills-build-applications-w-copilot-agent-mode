# OctoFit Tracker - Codespace Setup & API Testing Guide

## Overview

This guide covers how to setup and test the OctoFit Tracker API on GitHub Codespaces.

## Configuration Updates

The following changes have been made to support GitHub Codespace deployment:

### 1. **settings.py** - ALLOWED_HOSTS Configuration
- Added support for GitHub Codespace hostnames using the `$CODESPACE_NAME` environment variable
- Configured `ALLOWED_HOSTS` to accept:
  - `localhost`
  - `127.0.0.1`
  - `{$CODESPACE_NAME}-8000.app.github.dev`
  - `*` (wildcard for development)

### 2. **settings.py** - CORS Configuration
- Updated `CORS_ALLOWED_ORIGINS` to include Codespace URLs:
  - `https://{$CODESPACE_NAME}-8000.app.github.dev` (backend)
  - `https://{$CODESPACE_NAME}-3000.app.github.dev` (frontend)
- Set `CORS_ALLOW_ALL_ORIGINS = True` for development

### 3. **urls.py** - API Root View
- Updated `APIRootView` to properly handle HTTPS for Codespace deployments
- Detects secure connections and constructs proper URLs
- Returns base URL in response for easy reference

### 4. **.vscode/launch.json** - Django Launch Configuration
- Added `CODESPACE_NAME` environment variable to the launch configuration
- This allows Django to access the Codespace name at runtime

## How to Run the Server

### In GitHub Codespaces:

1. **Start the Django Backend:**
   - Open VS Code command palette: `Ctrl+Shift+D`
   - Select "Launch Django Backend" configuration
   - Server will start on `0.0.0.0:8000`

2. **Access the API:**
   - The API will be available at: `https://{$CODESPACE_NAME}-8000.app.github.dev/`
   - Replace `{$CODESPACE_NAME}` with your actual Codespace name
   - Example: `https://friendly-robot-8000.app.github.dev/`

### Locally:

1. **Activate Virtual Environment:**
   ```bash
   cd octofit-tracker/backend
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Start Django Server:**
   ```bash
   python manage.py runserver
   ```
   - Server will be available at `http://localhost:8000/`

## Testing the API

### Option 1: Using Provided Test Scripts

**On Linux/Mac:**
```bash
./test_api.sh
```

**On Windows:**
```cmd
test_api.bat
```

These scripts automatically detect the environment and test against:
- Codespace URL if `$CODESPACE_NAME` is set
- `localhost:8000` otherwise

### Option 2: Using curl Commands

Test individual endpoints:

```bash
# API Root
curl -k https://{$CODESPACE_NAME}-8000.app.github.dev/

# Users Endpoint
curl -k https://{$CODESPACE_NAME}-8000.app.github.dev/api/users/

# Activities Endpoint
curl -k https://{$CODESPACE_NAME}-8000.app.github.dev/api/activities/

# Teams Endpoint
curl -k https://{$CODESPACE_NAME}-8000.app.github.dev/api/teams/

# Workouts Endpoint
curl -k https://{$CODESPACE_NAME}-8000.app.github.dev/api/workouts/
```

**Note:** The `-k` flag is used to skip SSL certificate verification in development.

### Option 3: Using Codespaces Simple Browser

1. Once the server is running, VS Code will show a notification with the Codespace URL
2. Click the "Open in Browser" button or visit: `https://{$CODESPACE_NAME}-8000.app.github.dev/`

## API Endpoint Format

All REST API endpoints follow this pattern:

```
https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
```

**Available Endpoints:**
- `https://{$CODESPACE_NAME}-8000.app.github.dev/api/users/` - User management and profiles
- `https://{$CODESPACE_NAME}-8000.app.github.dev/api/activities/` - Activity logging and tracking
- `https://{$CODESPACE_NAME}-8000.app.github.dev/api/teams/` - Team management and leaderboards
- `https://{$CODESPACE_NAME}-8000.app.github.dev/api/workouts/` - Workout templates and plans
- `https://{$CODESPACE_NAME}-8000.app.github.dev/api/auth/` - Authentication endpoints

## Environment Variables

The following environment variables are used:

| Variable | Description | Example |
|----------|-------------|---------|
| `CODESPACE_NAME` | GitHub Codespace name (auto-set in Codespaces) | `friendly-robot` |
| `PYTHONPATH` | Python path (set in launch.json) | `/workspace/octofit-tracker/backend/venv/bin/python` |
| `VIRTUAL_ENV` | Virtual environment path (set in launch.json) | `/workspace/octofit-tracker/backend/venv` |

## Troubleshooting

### Certificate Warnings
When testing against HTTPS Codespace URLs, you may see certificate warnings. Use the `-k` flag in curl to skip verification:
```bash
curl -k https://{$CODESPACE_NAME}-8000.app.github.dev/
```

### 404 Errors
Ensure the database has been populated with test data. Run:
```bash
python manage.py populate_db
```

### CORS Issues
The configuration allows all origins for development. In production, update `CORS_ALLOWED_ORIGINS` with specific domains.

### Database Connection
Ensure MongoDB is running and configured properly in `settings.py`. The database uses djongo and should connect to `octofit_db`.

## Files Modified

- `octofit-tracker/backend/octofit_tracker/settings.py` - ALLOWED_HOSTS and CORS configuration
- `octofit-tracker/backend/octofit_tracker/urls.py` - API root view with scheme handling
- `.vscode/launch.json` - Django launch configuration with environment variables
- `test_api.sh` - Bash script for testing API endpoints
- `test_api.bat` - Windows batch script for testing API endpoints
