"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from config import redis_host,redis_password,redis_port,redis_db
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wme1h&*11s!m)5fb)yjo97zt=bx^s3^$bb*18-#a!00&=k9(4o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'corsheaders',#跨域用的
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Web.BasicFunctions',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',#跨域用的
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',#这边是Csrf
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR+"\\Web", 'BasicFunctions')],#这边要设置绝对路才能访问到templates文件
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

WSGI_APPLICATION = 'Web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'Medusa.db'),
    }
}

#跨域用的
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    'http://*',
    'https://*',
]

CORS_ALLOW_METHODS = (
    'GET',
    'OPTIONS',
    'POST',

)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'token',
    'x-requested-with',
    'Pragma',
)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/s/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'Web/Image'),#静态资源加载位置
    os.path.join(BASE_DIR,'Web/CrossSiteScriptHub/CrossSiteScriptProject'),#存放XSSjs文件目录
)


#celery
CELERY_RESULT_BACKEND='redis://:'+redis_password+'@'+redis_host+':'+redis_port+'/'+redis_db
CELERY_BROKER_URL='redis://:'+redis_password+'@'+redis_host+':'+redis_port+'/'+redis_db
'''

CELERY_RESULT_BACKEND='redis://:password@host:port/db'
host: Redis的服务器的名称或IP地址。例如 localhost:本地主机。
port: Redis的服务器。默认值是6379
db: 使用的数据库数,默认值为0
password: 密码用于连接到数据库。

缓存后端设置
使用单个memcached服务器：
CELERY_RESULT_BACKEND='cache+memcached://127.0.0.1:11211/'
cache : 缓存
'''
CELERY_ACCEPT_CONTENT=['json']
CELERY_TASK_SERIALIZER='json'


#上传图片最大值设置
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485761