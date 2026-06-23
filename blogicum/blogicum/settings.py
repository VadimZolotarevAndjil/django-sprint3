from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


<<<<<<< HEAD
SECRET_KEY = "django-insecure-@j3v(_a%^n7ai_8*)h*bqeaplt19k4)k6hyr1xk841!3hmk4^+"
=======
SECRET_KEY = 'django-insecure-@j3v(_a%^n7ai_8*)h*bqeaplt19k4)k6hyr1xk841!3hmk4^+'
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
<<<<<<< HEAD
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog.apps.BlogConfig",
    "pages.apps.PagesConfig",
    "debug_toolbar",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

ROOT_URLCONF = "blogicum.urls"

TEMPLATE_DIRS = [
    BASE_DIR / "templates",
=======
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'pages.apps.PagesConfig',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
] 

ROOT_URLCONF = 'blogicum.urls'

TEMPLATE_DIRS = [
    BASE_DIR / 'templates',
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
]

TEMPLATES = [
    {
<<<<<<< HEAD
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": TEMPLATE_DIRS,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
=======
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
            ],
        },
    },
]

<<<<<<< HEAD
WSGI_APPLICATION = "blogicum.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
=======
WSGI_APPLICATION = 'blogicum.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
<<<<<<< HEAD
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
=======
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
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
    },
]


<<<<<<< HEAD
LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "UTC"
=======
LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73

USE_I18N = True

USE_L10N = True

USE_TZ = True


<<<<<<< HEAD
STATIC_URL = "/static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_DIRS = [BASE_DIR / "static_dev"]
=======
STATIC_URL = '/static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / 'static_dev'
]
>>>>>>> c2dcd87c5f95dbc38b900f2ea7432dd76344ee73
