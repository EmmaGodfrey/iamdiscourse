import os
import dj_database_url
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY', default='your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

# SECURITY WARNING: define allowed hosts
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=lambda v: [
                       s.strip() for s in v.split(',')])

# Database configuration
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('Postgres.DATABASE_URL'),
        conn_max_age=1800
    )
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library',  # Ensure your app is listed here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iamdiscourse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iamdiscourse.wsgi.application'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.environ["RAILWAY_VOLUME_MOUNT_PATH"]

# Security settings
CSRF_COOKIE_SECURE = True 
SESSION_COOKIE_SECURE = True 
X_FRAME_OPTIONS = 'DENY'
CSRF_TRUSTED_ORIGINS = [
    'https://theiamdiscourses.org', 'https://theiamdiscourses.up.railway.app']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Optional Jazzmin configuration
JAZZMIN_SETTINGS = {
    "site_title": "IamDiscourses",
    "site_header": "IamDiscourses",
    "site_brand": "IamDiscourses",
    "welcome_sign": "Welcome to the IamDiscourses Admin",
    "copyright": "Aimabeing",
    "topmenu_links": [
        {"name": "Home", "url": "/", "new_window": True},
        {"name": "Logout", "url": "/logout/", "new_window": False},
    ],
}

LOGOUT_REDIRECT_URL = 'logout'
