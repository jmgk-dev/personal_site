# Personal Site / jmgk.dev

## Description
This is a personal portfolio site built for my own work using Python, Django and PostgreSQL. Functionality for uploading projects with images and descriptions is included. The site is responsive and works on all devices.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Contact Information](#contact-information)

## Installation
Provide step-by-step instructions on how to get the development environment running.

# Clone the repo
```bash
git clone https://github.com/jmgk-dev/personal_site.git
```

# Navigate to the project directory
```bash
cd personal_site
```

# Create a virtual environment
```bash
python3 -m venv venv
```

# Activate the virtual environment
```bash
source venv/bin/activate
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Switch settings to dev
```bash
export DJANGO_SETTINGS_MODULE=personal_site.settings.dev
```

# Create PostgreSQL database and user
```bash
sudo -u postgres psql
CREATE DATABASE <myproject>;
CREATE USER <myprojectuser> WITH PASSWORD 'password';
ALTER ROLE <myprojectuser> SET client_encoding TO 'utf8';
ALTER ROLE <myprojectuser> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <myprojectuser> SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE <myproject> TO <myprojectuser>;
```
# Enable user to run tests
```bash
ALTER USER <myprojectuser> WITH CREATEDB;
```
# Enable user to create tables
```bash
\connect <myproject>
GRANT ALL ON SCHEMA public TO <myprojectuser>;
```

# Quit PostgreSQL
```bash
\q
```
# Create a secret key for production and add it to a new .env
```bash
echo "DJANGO_DEV_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" >> .env && \
echo "DJANGO_SECURE_PRODUCTION_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" >> .env
```

# Add the below to .env replacing values
```bash
DATABASE_SERVICE=<database_name>
DATABASE_NAME=<database_name>
DATABASE_USER=<database_user>
DATABASE_PASSWORD=<database_password>
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

# Also add for Bugsnag if you wish to use
```bash
BUGSNAG_API_KEY=<BUGSNAG_API_KEY>
PATH_TO_YOUR_APP=<PATH_TO_YOUR_APP>
```

# Migrate the database
```bash
python manage.py migrate
```

# Start the development server
```bash
python manage.py runserver
```

# Create superuser
```bash
python manage.py createsuperuser
```


## Usage
Instructions on how to use the project.
```bash
# Example of how to use the project
```


## Contact Information
```
jamie@jmgk.dev
```

