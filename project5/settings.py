"""
Django Settings for project5.
Base code: 'Boutique Ado' (Code Institute's walk-through)
Modernized for Django 4.2 - with ChatGPT's guidance, to improve 'Best Practices'
"""

import os
from pathlib import Path
import dj_database_url

# Load Environment variables if env.py exists
if os.path.isfile('env.py'):
    import env


# Paths
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEVELOPMENT' in os.environ

# Allowed Hosts
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'kellys-art-and-photo-boutique-913058c0223e.herokuapp.com',
]


# CSRF Trusted Origins - adjusted with ChatGPT's guidance
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
    "https://localhost:8000",
    "https://*.herokuapp.com"
]


# Applications - rearranged with ChatGPT's guidance - to improve Best Practices
INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third-party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'storages',
    'csp',

    # Kelly's Art & Photo Boutique's apps
    'home',
    'products',
    'cart',
    'checkout',
    'profiles',
    'howto',
    'contact',
    'newsletter', 
]


# Middleware - fixed with ChatGPT's guidance - to fix AWS and CSP
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Content Security Policy (CSP) for Django-csp - copied exactly from ChatGPT - to improve Best Practices
CSP_DIRECTIVES = {
    "default-src": ("'self'",),
    "script-src": (
        "'self'",
        "'unsafe-inline'",
        "'unsafe-eval'",
        "https://js.stripe.com",
        "https://cdnjs.cloudflare.com",
        "https://cdn.jsdelivr.net",
        "https://kellys-art-and-photo-boutique.s3.amazonaws.com",
    ),
    "style-src": (
        "'self'",
        "'unsafe-inline'",
        "https://fonts.googleapis.com",
        "https://cdnjs.cloudflare.com",
        "https://cdn.jsdelivr.net",
        "https://kellys-art-and-photo-boutique.s3.amazonaws.com",
    ),
    "font-src": (
        "'self'",
        "https://fonts.gstatic.com",
        "https://kellys-art-and-photo-boutique.s3.amazonaws.com",
    ),
    "img-src": (
        "'self'",
        "data:",
        "https://res.cloudinary.com",
        "https://kellys-art-and-photo-boutique.s3.amazonaws.com",
        "https://kellys-art-and-photo-boutique.s3.eu-north-1.amazonaws.com",
    ),
    "connect-src": (
        "'self'",
        "https://api.stripe.com",
    ),
    "frame-src": (
        "https://js.stripe.com",
    ),
    "base-uri": ("'self'",),
    "object-src": ("'none'",),
    "form-action": (
        "'self'",
        "https://js.stripe.com"),
    "manifest-src": ("'self'",),
}


# Security settings for styling to work locally and otherwise - fixed with ChatGPT's guidance
if 'DEVELOPMENT' in os.environ:
    # Local development - copied from ChatGPT
    DEBUG = True
    SECURE_HSTS_SECONDS = 0
    SECURE_SSL_REDIRECT = False
    SECURE_CONTENT_TYPE_NOSNIFF = False
    SECURE_BROWSER_XSS_FILTER = False
    X_FRAME_OPTIONS = 'SAMEORIGIN'  # allows iframe in dev if needed

    # Email (local)
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = '2025studentproject@gmail.com'

else:
    # Production - copied from ChatGPT
    DEBUG = False
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'

    # Email (Production)
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')


# Templates
CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', # required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'cart.contexts.cart_contents',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]


# Authentication Backends
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


# URL and WSGI
ROOT_URLCONF = 'project5.urls'
WSGI_APPLICATION = 'project5.wsgi.application'


# Database
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


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
USE_L10N = True
USE_TZ = True


# Static and Media files (CSS, JavaScript, Images) - fixed with ChatGPT's guidance
USE_AWS = os.environ.get('USE_AWS', False)

if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'kellys-art-and-photo-boutique'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'project5.custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'project5.custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

else:
    # Local static and media - moved with ChatGPT's guidance as css not ok locally after cps fix
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    # WhiteNoise: compress and cache static files for Heroku - added with ChatGPT's guidance, to fix css issue
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Stripe
FREE_POSTAGE_THRESHOLD = 33
STANDARD_POSTAGE_PERCENTAGE = 11
STRIPE_CURRENCY = 'eur'
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_WH_SECRET = os.environ.get('STRIPE_WH_SECRET')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
