# Django settings for cseismic2kx project.
import os

ROOT_DIR = os.path.dirname(__file__)

try:
    import localsettings
except ImportError:
    print "Define Localsettings"
    raise ImportError

DEBUG = localsettings.DEBUG
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = localsettings.DATABASES

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Kolkata'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-in'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(ROOT_DIR, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*uhik@ffpc96vlg*k%*@==o_w+lc+4eijhpu^t+x%fdp!d*vxi'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.request',
        'django_authopenid.context_processors.authopenid',
        )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'cseismic2kx.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_DIR, 'templates'),
)

ACCOUNT_ACTIVATION_DAYS = 10
LOGIN_URL = '/account/signin'
LOGOUT_URL = '/account/signout'
LOGIN_REDIRECT_URL = '/'
REGISTRATION_OPEN = True
AUTH_PROFILE_MODULE = 'participantsprofile.UserProfile'

DEFAULT_FROM_EMAIL = 'no-reply@cseismic2k10.co.cc'

INSTALLED_APPS = (
    'cseismic2kx.reporting',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'south',
    'django_authopenid',
    
    'cseismic2kx.home',
    'cseismic2kx.events',
    'cseismic2kx.host',
    'cseismic2kx.registration',
    'cseismic2kx.participantsprofile',
    'cseismic2kx.captcha',
)
