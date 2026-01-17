# Security Setup Guide

## Environment Variables Configuration

This application uses environment variables to securely manage sensitive credentials. **Never commit actual credentials to version control.**

### Required Environment Variables

#### Development Mode
When `DEVELOPMENT_MODE=True`, you need to set:

- `DB_NAME` - Database name (default: "test")
- `DB_USER` - Database user (default: "postgres")
- `DB_PASSWORD` - **REQUIRED** - Database password (no default)
- `DB_HOST` - Database host (default: "localhost")
- `DB_PORT` - Database port (default: "5432")

#### Production Mode
When `DEVELOPMENT_MODE=False`:

- `DATABASE_URL` - Full database connection URL (format: `postgresql://user:password@host:port/database`)

#### Email Configuration
For all modes:

- `EMAIL_HOST_USER` - SMTP email address (default: "stockdocksoftware@gmail.com")
- `EMAIL_HOST_PASSWORD` - **REQUIRED** - Email account app password (no default)

#### Django Settings
- `DJANGO_SECRET_KEY` - Django secret key (auto-generated if not set)
- `DEBUG` - Enable debug mode (default: "False")
- `DJANGO_ALLOWED_HOSTS` - Comma-separated allowed hosts (default: "127.0.0.1,localhost")

### Setup Instructions

1. Copy `.env.example` to `.env` in the `webApp_PrintSoftware` directory:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and fill in your actual credentials:
   ```bash
   # Example .env content
   DEVELOPMENT_MODE=True
   DB_PASSWORD=your_actual_database_password
   EMAIL_HOST_PASSWORD=your_actual_email_app_password
   ```

3. **Never commit the `.env` file** - it's already in `.gitignore`

### Security Notes

- The `.env` file is excluded from version control via `.gitignore`
- All sensitive credentials should be stored in environment variables
- In production, use your hosting platform's environment variable configuration (e.g., Heroku Config Vars, AWS Systems Manager, etc.)
- For Gmail SMTP, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your account password
