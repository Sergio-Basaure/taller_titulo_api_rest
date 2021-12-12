from datetime import timedelta
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a96^-^k(-9-#hri=dld^a946##h1xw(+k++__%-#@^m)ft5^q='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'cliente',
    'local',
    'productos',
    'servicios',
    'usuario',
    'codigo_qr',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',

    # 'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
    'drf_yasg',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 12,
    # 'DEFAULT_PERMISSION_CLASSES' : (
    #     'rest_framawork.permissions.IsAuthenticated' # para bloquear todo con token
    # )
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

ROOT_URLCONF = 'ccs_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ccs_api.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'cliente.Cliente'

DATE_INPUT_FORMATS = ['%d-%m-%Y']
TIME_INPUT_FORMATS = ['%H:%M']


CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS  =  [
    "http://localhost:8080" ,  
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080" , 
]

SIMPLE_JWT = { 
    'ACCESS_TOKEN_LIFETIME' : timedelta(days=1),
    'ACCESS_TOKEN_LIFETIME' : timedelta(days=1),
    'ROTATE_REFRESH_TOKENS' : True,
    'BLACKLIST_AFTER_ROTATION' : True
    }

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Chile/Continental'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# para realizar peticion put por app mediante qr
# APPEND_SLASH=False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Emails
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tallerciisaccs@gmail.com'
EMAIL_HOST_PASSWORD = 'taller1234'
EMAIL_USE_TLS = True