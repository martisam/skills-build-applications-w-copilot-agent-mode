# OctoFit Tracker Backend

Django REST API for the OctoFit Tracker fitness application.

## Project Structure

```
backend/
├── manage.py                 # Django management script
├── octofit_tracker_core/    # Main Django project
├── users/                    # User profiles app
├── activities/               # Activity logging app
├── teams/                    # Team management app
├── workouts/                 # Workout templates & plans app
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore file
└── venv/                    # Virtual environment
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Migrations

```bash
python manage.py makemigrations
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Populate Database with Sample Data

```bash
python manage.py populate_db
```

This command creates:
- 6 sample users
- User profiles with fitness information
- 30-90 sample activities across all types
- 6 workout templates
- 3 teams with members
- Team leaderboards
- 6 personalized workout plans

### 7. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 8. Run Development Server

```bash
python manage.py runserver
```

The server will run on `http://localhost:8000`

## API Documentation

### Available Endpoints

- **Admin Panel:** `http://localhost:8000/admin/`
- **API Auth:** `/api-auth/`
- **Auth Endpoints:** `/api/auth/` (login, logout, user details)
- **Auth Registration:** `/api/auth/registration/`

### Apps & Models

#### Users App
- **UserProfile** - Extended user information (fitness level, stats, etc.)

#### Activities App
- **Activity** - Individual exercise/activity logs

#### Teams App
- **Team** - Team management and creation
- **TeamMembership** - User roles within teams
- **Leaderboard** - Team competition leaderboard
- **LeaderboardEntry** - Individual leaderboard standings

#### Workouts App
- **Workout** - Workout templates
- **WorkoutPlan** - Personalized user workout plans
- **WorkoutPlanDay** - Daily workout assignments

## Database

This project uses **MongoDB** via Djongo as the primary database.

**Connection Details:**
- Host: `localhost`
- Port: `27017`
- Database: `octofit_tracker_db`

Ensure MongoDB is running before starting the Django server:
```bash
# Check if mongod is running
ps aux | grep mongod
```

## Technologies

- **Django** 4.1.7 - Web framework
- **Django REST Framework** 3.14.0 - REST API
- **Djongo** 1.3.6 - MongoDB ORM
- **MongoDB** - Database
- **django-allauth** - Authentication
- **dj-rest-auth** - DRF auth endpoints
- **django-cors-headers** - CORS support

## Environment Variables

Create a `.env` file in the backend directory:

```
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
MONGODB_HOST=localhost
MONGODB_PORT=27017
```

## Admin Credentials

After running `python manage.py createsuperuser`, use the credentials to access the admin panel at `/admin/`

## Development

### Create New App

```bash
python manage.py startapp app_name
```

### Run Tests

```bash
python manage.py test
```

### Collect Static Files

```bash
python manage.py collectstatic
```

## Troubleshooting

### Long Path Issues (Windows)

If you encounter path length errors, enable long path support:
```powershell
reg add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /d 1 /f
```

### MongoDB Connection Issues

- Ensure MongoDB is running: `mongod`
- Check connection in Django admin panel
- Verify database name in `settings.py`

### Migration Issues

```bash
# Reset migrations (careful with data loss!)
python manage.py migrate --fake-initial
```

## Production Deployment

1. Set `DEBUG=False` in settings
2. Update `ALLOWED_HOSTS` with your domain
3. Use environment variables for sensitive data
4. Configure CORS for frontend domain
5. Set up proper logging
6. Configure HTTPS
7. Use a production WSGI server (Gunicorn)

## Support

For issues and questions, refer to the main project documentation.
