# Django Todo Application

A Django-based todo application with user authentication and AI-powered task summaries.

## Recent Fixes Applied

### Critical Issues Fixed:

1. **Login Import Issue** - Fixed function name conflict in `accounts/views.py`
2. **User Model** - Removed redundant password field from custom User model
3. **Task Model** - Removed redundant id field (Django auto-creates this)
4. **OpenAI Integration** - Fixed API calls and made client initialization conditional
5. **Error Handling** - Added proper try-catch blocks for database operations
6. **Security** - Added `@login_required` decorators to protected views
7. **Dependencies** - Added missing packages to requirements.txt

### Security Improvements:

- Added proper user authentication checks
- Protected task operations with login_required decorators
- Added user ownership validation for task operations
- Improved error handling to prevent information leakage

### Code Quality Improvements:

- Fixed inconsistent indentation
- Added proper imports
- Improved function naming
- Added comprehensive error handling

## Setup Instructions

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:

   ```bash
   python manage.py migrate
   ```

3. Create a superuser (optional):

   ```bash
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Environment Variables

Create a `.env` file in the project root with:

```
SECRET_KEY=your-secret-key-here
OPENAI_API_KEY=your-openai-api-key-here  # Optional for AI summaries
```

## Features

- User registration and authentication
- Create, edit, delete, and mark tasks as complete
- Archive completed tasks
- Guest mode for anonymous users
- AI-powered daily summaries (requires OpenAI API key)
- Responsive Bootstrap UI

## Security Notes

- The SECRET_KEY should be moved to environment variables in production
- All task operations are now properly protected with user authentication
- Database queries include user ownership validation
