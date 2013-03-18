import os
# Django settings for bentyne project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

ADMINS = (
        # ('Your Name', 'your_email@example.com'),
        )

MANAGERS = ADMINS

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'test_bentyne.db',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
            }
        }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/El_Salvador'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = 'media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
        # Put strings here, like "/home/html/static" or "C:/www/django/static".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
        )

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^j&amp;+==9f6c0a5o8b++gs7pxt=393ptb0vrmud$aq9wfh6x3y+^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        #     'django.template.loaders.eggs.Loader',
        )

MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        # Uncomment the next line for simple clickjacking protection:
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ## mediagenerator
        'mediagenerator.middleware.MediaMiddleware',
        'accounts.middleware.RequireLoginMiddleware'
        )

ROOT_URLCONF = 'bentyne.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'bentyne.wsgi.application'


INSTALLED_APPS = (
        'themes',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.markup',
        'skylark',
        'brasil',
        'django.contrib.comments',
        'cheryl',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin',
        'django_extensions',
        'debug_toolbar',
        'mediagenerator',
        'mptt',
        'taggit',
        'oriel',
        'userena',
        'easy_thumbnails',
        'guardian',
        'accounts',
        # Uncomment the next line to enable admin documentation:
        # 'django.contrib.admindocs',
        )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
                }
            },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
                }
            },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
                },
            }
        }

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
        )

# MediaGenerator

MEDIA_DEV_MOD = DEBUG
DEV_MEDIA_URL = '/devstuff/'
PRODUCTION_MEDIA_URL = '/stuff/'

GLOBAL_MEDIA_DIRS = ('skylarkmedia', )


MEDIA_BUNDLES = (
        ('foundation.css',
            'foundation/stylesheets/foundation.css',
            'foundation/stylesheets/app.css',
            ),
        ('foundation.js',
            'libs/jquery.js',
            'foundation/javascripts/foundation.min.js',
            'foundation/javascripts/jquery.foundation.topbar.js',
            'foundation/javascripts/jquery.placeholder.js',
            ),
        ('raptor.js',
            'libs/raptor.0deps.min.js',
            ),
        ('redactor.js',
            'libs/redactor/redactor/redactor.js',
            ),
        ('redactor.css',
            'libs/redactor/redactor/redactor.css',
            ),
        ('main.js',
            'libs/jquery.js',
            'foundation/javascripts/foundation.min.js',
            'foundation/javascripts/jquery.foundation.topbar.js',
            ),
        ('jqtree.js',
            'libs/jqtree/tree.jquery.js',
            ),
        ('jqtree.css',
            'libs/jqtree/jqtree.css',
            ),
        )

AUTHENTICATION_BACKENDS = (
        'userena.backends.UserenaAuthenticationBackend',
        'guardian.backends.ObjectPermissionBackend',
        'django.contrib.auth.backends.ModelBackend',
        )

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'



EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'r.ascencio.py@gmail.com'
EMAIL_HOST_PASSWORD = '45lotengo++56lo56lo56lo.l'




ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'accounts.BentyneUsers'
LOGIN_REDIRECT_URL = '/auth/%(username)s/'
USERENA_SIGNIN_REDIRECT_URL = '/skylark/'


LOGIN_URL = '/auth/signin/'
LOGOUT_URL = '/auth/signout/'
USERENA_ACTIVATION_REQUIRED = False


THEME_DIRS = ('themes/',
        )


LOGIN_REQUIRED_URLS = (
    r'/skylark/(.*)$',
)

LOGIN_REQUIRED_URLS_EXCEPTIONS = (
        ''
)


try:
    from skylark.models import Settings
except:
    pass

try:
    SKYLARK_SETTINGS = Settings.objects.get(id=1)
except:
    pass

try:
    TEMPLATE_DIRS = (
        os.path.join(PROJECT_ROOT, 'themes', SKYLARK_SETTINGS.site_theme)
        )
except:
    TEMPLATE_DIRS = (
        os.path.join(PROJECT_ROOT, 'themes', 'theme2'),
        )

