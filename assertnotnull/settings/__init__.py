# Django settings for electionquebec project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

SITE_ROOT = '/'.join(os.path.dirname(__file__).split('/')[0:-2])
LOGS_ROOT = os.path.join(SITE_ROOT, 'logs')

backup_count = 1000
if DEBUG:
    backup_count = 2

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Montreal'

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# A boolean that turns on/off debug mode. When set to ``True``, stack traces
# are displayed for error pages. Should always be set to ``False`` in
# production. Best set to ``True`` in local_settings.py
DEBUG = False

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1

SITE_ROOT = '/'.join(os.path.dirname(__file__).split('/')[0:-2])

LOGS_ROOT = os.path.join(SITE_ROOT, 'logs')

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# URL prefix for static files.
# Example: 'http://media.lawrence.com/static/'
STATIC_URL = '/static/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' 'static/' subdirectories and in STATICFILES_DIRS.
# Example: '/home/media/media.lawrence.com/static/'
#STATIC_ROOT = ''
STATIC_ROOT = os.path.join(SITE_ROOT, STATIC_URL.strip('/'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: 'http://media.lawrence.com/media/', 'http://example.com/media/'
#MEDIA_URL = ''
MEDIA_URL = STATIC_URL + 'media/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: '/home/media/media.lawrence.com/media/'
#MEDIA_ROOT = ''
MEDIA_ROOT = os.path.join(SITE_ROOT, *MEDIA_URL.strip('/').split('/'))

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: 'http://foo.com/static/admin/', '/static/admin/'.
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'

SITE_PREFIX = 'blog'

# Additional locations of static files
STATICFILES_DIRS = (
# Put strings here, like '/home/html/static' or 'C:/www/django/static'.
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
)

# If True, the south application will be automatically added to the
# INSTALLED_APPS setting.
USE_SOUTH = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'uj-yunk8m$8wgefskf9lftl6@yk_^8viumykk4zj4_qv&=7m6o'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

AUTHENTICATION_BACKENDS = ('mezzanine.core.auth_backends.MezzanineBackend',)

ROOT_URLCONF = 'assertnotnull.urls'

TEMPLATE_DIRS = (
    # Put strings here, like '/home/html/django_templates' or 'C:/www/django/templates'.
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(SITE_ROOT, 'templates'),
    )

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = 'filebrowser_safe'
PACKAGE_NAME_GRAPPELLI = 'grappelli_safe'

################
# APPLICATIONS #
################

INSTALLED_APPS = (
    'mezzanine_themes.assertnotnull',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'twitter_tag',
    'mezzanine.boot',
    'mezzanine.conf',
    'mezzanine.core',
    'mezzanine.generic',
    'mezzanine.blog',
    'mezzanine.forms',
    'mezzanine.pages',
    'mezzanine.galleries',
    'mezzanine.twitter',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
#    'django.contrib.admindocs',
    'apps.base',
    )

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.tz',
    'mezzanine.conf.context_processors.settings',
)

# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES = (
    'mezzanine.core.middleware.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'mezzanine.core.request.CurrentRequestMiddleware',
    'mezzanine.core.middleware.TemplateForDeviceMiddleware',
    'mezzanine.core.middleware.TemplateForHostMiddleware',
    'mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware',
    # Uncomment the following if using any of the SSL settings:
    # 'mezzanine.core.middleware.SSLRedirectMiddleware',
    'mezzanine.pages.middleware.PageMiddleware',
    'mezzanine.core.middleware.FetchFromCacheMiddleware',
    )

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = 'filebrowser_safe'
PACKAGE_NAME_GRAPPELLI = 'grappelli_safe'


#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    'debug_toolbar',
    'django_extensions',
    'compressor',
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
    )

DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'base': {
            'format' : '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt' : '%d/%b/%Y %H:%M:%S'
        },
        },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
            },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter' : 'base',
            },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, 'main.log'),
            'maxBytes': 50000,
            'backupCount': backup_count,
            'formatter': 'base',
            },
        'db': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_ROOT, 'db.log'),
            'maxBytes': 50000,
            'backupCount': backup_count,
            'formatter': 'base',
            },
        },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        'circonscriptions.management.commands.loadshapefiles': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            }
    },
}
