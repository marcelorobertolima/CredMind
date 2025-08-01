"""
Django settings for pCredMind project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3j+qcco&3(3wr^p$p30h7x6-@d!$s12vzt(2ekgnq961q%jl)f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'APICredMind',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pCredMind.urls'

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

WSGI_APPLICATION = 'pCredMind.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'CredMind',
        'USER': 'marcelo.lima',
        'PASSWORD': 'Polac@2901',
        'HOST': '192.168.2.253\\MSSQL19',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+n$39z+wac^z$+2trm2u1=()gdczx$!ox#xpxjhdy&6*@(t+r6'

AUTH_USER_MODEL = 'APICredMind.CustomUser'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),  # Tempo de vida do token de acesso (24 horas)
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),  # Tempo de vida do token de atualização (30 dias)
    'ROTATE_REFRESH_TOKENS': True,  # Rotacionar tokens de atualização
    'BLACKLIST_AFTER_ROTATION': True,  # Colocar tokens antigos na blacklist após rotação
    'ALGORITHM': 'HS256',  # Algoritmo de codificação JWT
    'SIGNING_KEY': SECRET_KEY,  # Chave secreta para assinatura JWT
    'AUTH_HEADER_TYPES': ('Bearer',),  # Tipos de cabeçalho de autenticação
    'USER_ID_FIELD': 'id',  # Campo de ID do usuário
    'USER_ID_CLAIM': 'user_id',  # Reivindicação do ID do usuário no token
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',  # Reivindicação do tipo de token
    'JTI_CLAIM': 'jti',  # Reivindicação do JTI (ID do token)
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',  # Reivindicação do tempo de expiração do token de atualização
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),  # Tempo de vida do token de acesso ao usar atualização contínua
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),  # Tempo de vida do token de atualização ao usar atualização contínua
}

AUTHENTICATION_BACKENDS = [
    'APICredMind.authentication.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',  # Certifique-se de manter o backend padrão também
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
