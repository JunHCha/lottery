"""
Django settings for lotterypjt project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+#_at%9^!y@cp7b95)t+=y@p1-v34wy3$dn^$1dfa+ye$08f*2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost', '.ap-northeast-2.compute.amazonaws.com', '.lottery-unist.ml',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lotteryapp',
    'user',
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

ROOT_URLCONF = 'lotterypjt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #Base template 여기에 추가해놨습니다!
        'DIRS': [os.path.join(BASE_DIR), 'lotterypjt/templates'],
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

WSGI_APPLICATION = 'lotterypjt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Static file URL 고정값 {% static '경로' %} == STATIC_URL+'경로'
STATIC_URL = '/static/'
# Base_dir/static -> static 파일 여기서 찾아요
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
#Deploy할때, 흩어져있는 static파일을 특정 디렉토리에 옮기기
#manage.py collectstatic 필수
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 이메일 호스트 설정
EMAIL_HOST = 'smtp.gmail.com'                # 메일 호스트 서버
EMAIL_PORT = '587'                           # 서버 포트
EMAIL_HOST_USER = 'uni.mutsa2020@gmail.com'  # 우리가 사용할 Gmail
EMAIL_HOST_PASSWORD = '!uni1q2w3e4r'       # 우리가 사용할 Gmail p
EMAIL_USE_TLS = True                      # TLS 보안 설정
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER        # 응답 메일 관련 설정