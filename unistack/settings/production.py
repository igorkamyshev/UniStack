DEBUG = False

ALLOWED_HOSTS = [
    'thegarik.pythonanywhere.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TheGarik$unistack',
        'USER': 'TheGarik',
        'PASSWORD': 'unistack1488',
        'HOST': 'TheGarik.mysql.pythonanywhere-services.com'
    }
}