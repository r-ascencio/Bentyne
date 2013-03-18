import os
# Django settings for bentyne project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG


PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
# /

ADMINS = (
        # ('Your Name', 'your_email@example.com'),
        )

MANAGERS = ADMINS

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'rascenciomedb',                      # Or path to database file if using sqlite3.
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
STATIC_ROOT = 'static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
# STATICFILES_DIRS = (
#         os.path.join(PROJECT_ROOT, '_generated_media'),
#         # Put strings here, like "/home/html/static" or "C:/www/django/static".
#         # Always use forward slashes, even on Windows.
#         # Don't forget to use absolute paths, not relative paths.
#         )


# List of finder classes that know how to find static files in
# various locations.

GLOBAL_MEDIA_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)

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
        'django.contrib.comments',
        'haystack',
        # 'django-haystack',
        'django_extensions',
        'debug_toolbar',
        'mediagenerator',
        'mptt',
        'taggit',
        'easy_thumbnails',
        'guardian',
        'accounts',
        )
INSTALLED_APPS += (
        'brasil',
        'oriel',
        'skylark',
        'cheryl',
        'userena',
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

# INTERNAL_IPS = ('127.0.0.1',)

# DEBUG_TOOLBAR_PANELS = (
#         'debug_toolbar.panels.version.VersionDebugPanel',
#         'debug_toolbar.panels.timer.TimerDebugPanel',
#         'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
#         'debug_toolbar.panels.headers.HeaderDebugPanel',
#         'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
#         'debug_toolbar.panels.template.TemplateDebugPanel',
#         'debug_toolbar.panels.sql.SQLDebugPanel',
#         'debug_toolbar.panels.signals.SignalDebugPanel',
#         'debug_toolbar.panels.logger.LoggingPanel',
#         )

INTERCEPT_REDIRECTS = False
# MediaGenerator

MEDIA_BUNDLES = (
        ('foundation.css',
            'foundation/stylesheets/foundation.css',
            'foundation/stylesheets/app.css',
            ),
        ('foundation.js',
            'foundation/javascripts/foundation.min.js',
            'foundation/javascripts/jquery.foundation.topbar.js',
            'foundation/javascripts/jquery.placeholder.js',
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
        ('jquery.js',
            'libs/jquery.js',
            ),
        ('colorbox.js',
            'libs/colorbox/jquery.colorbox.js',
            ),
        ('colorbox.css',
            'libs/colorbox/colorbox.css',
            ),
        ('nivo.css',
            'libs/nivo-slider/nivo-slider.css',
            ),
        ('nivo.js',
            'libs/nivo-slider/jquery.nivo.slider.pack.js',
            ),
        ('nivo-default.css',
            'libs/nivo-slider/themes/default/default.css',
            ),
        ('nivo-bar.css',
            'libs/nivo-slider/themes/bar/bar.css',
            ),
        ('nivo-dark.css',
            'libs/nivo-slider/themes/dark/dark.css',
            ),
        ('nivo-light.css',
            'libs/nivo-slider/themes/light/light.css',
            ),
        ('galleria.js',
            'libs/galleria/galleria-1.2.8.min.js',
            ),
        ('galleria-theme.js',
            'libs/galleria/themes/classic/galleria.classic.min.js',
            ),
        ('galleria-theme.css',
            'libs/galleria/themes/classic/galleria.classic.css',
            ),
        ('raptor.js',
            'libs/raptor.0deps.min.js',
            # 'libs/jquery-two.js',
            ),
        # ('galleria.js',
        #     'libs/galleria/galleria-1.2.8.min.js',
        #     ),
        # ('jquery-file-upload.js',
        #     ),
        # css/bootstrap.min.css
        # css/style.css
        # css/bootstrap-responsive.min.css
        # css/bootstrap-image-gallery.min.css
        # css/jquery.fileupload-ui.css
        )


MEDIA_DEV_MOD = DEBUG
DEV_MEDIA_URL = '/devstuff/'
PRODUCTION_MEDIA_URL = '/stuff/'



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


HAYSTACK_SITECONF = 'bentyne.search_sites'

HAYSTACK_SEARCH_ENGINE = 'whoosh'

HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_ROOT, 'search', 'whoosh_index')

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5


THEME_DIRS = ('themes/',
        )


LOGIN_REQUIRED_URLS = (
    r'/skylark/(.*)$',
    r'/auth/signup/$',
    r'/auth/$',
)

LOGIN_REQUIRED_URLS_EXCEPTIONS = (
        ''
)


try:
    from skylark.models import Settings as confs
except:
    pass
try:
    SKYLARK_SETTINGS = confs.objects.get(id=1)
except:
    pass

try:
    TEMPLATE_DIRS = (
        os.path.join(PROJECT_ROOT, 'themes', SKYLARK_SETTINGS.site_theme)
        )
except:
    TEMPLATE_DIRS = (
        os.path.join(PROJECT_ROOT, 'themes', 'default'),
        )


try:
    STATICFILES_DIRS = (
            os.path.join(PROJECT_ROOT, 'themes', SKYLARK_SETTINGS.site_theme, 'static'),
            os.path.join(PROJECT_ROOT, '_generated_media'),
            )
except:
    print "static theme dont work"

TEMPLATE_CONTEXT_PROCESSORS = (
            # "django.core.context_processors.auth",
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.request',
            "django.core.context_processors.debug",
            "django.core.context_processors.i18n",
            "django.core.context_processors.media",
            # 'django.template.Variable.resolve',
            'django.core.context_processors.static'
            )

DEBUG_TOOLBAR_CONFIG = {
            'INTERCEPT_REDIRECTS': False,
            }




# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#         'URL': 'http://127.0.0.1:9200/',
#         'INDEX_NAME': 'haystack',
#     },
# }



#ThemeChangued
#ThemeChangued
#ThemeChangued
#ThemeChangued
#ThemeChangued
#ThemeChangued
#ThemeChangued
#ThemeChangued
