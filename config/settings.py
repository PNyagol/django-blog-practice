from pathlib import Path
import os

# Base directory for the project

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# User-uploaded files go here
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# The URL that points to the above location
MEDIA_URL = '/media/'

# Keep this secret key secure (use environment variables in production)



SECRET_KEY = 'django-insecure-)&kks(s#u8!ytv&x#jbscopxlw&a@#*y9*3u^z1os)wwc3p%wx'

# Enable debug mode for development only

DEBUG = True

# Hosts allowed to serve this app

ALLOWED_HOSTS = []

# Installed Django apps



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'atugi',
]


# Middleware stack (request/response processing)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URL configuration module
ROOT_URLCONF = 'config.urls'


# Template engine configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# WSGI application path
WSGI_APPLICATION = 'config.wsgi.application'




# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'blog.sqlite3'),
    }
}




# Password validation rules
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




# Internationalization settings
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




# Static files URL
STATIC_URL = 'static/'

# Static files directories
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
