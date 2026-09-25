import os
from dotenv import load_dotenv


load_dotenv()
adress_db = os.getenv('HOST')
password_db = os.getenv('PASSWORD')
secret_key = os.getenv('SECRET_KEY')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': adress_db,
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': password_db,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True