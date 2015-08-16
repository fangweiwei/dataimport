"""
Django settings for fileupload project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6dgv@+03d$xc#c$bexd)$(z85m@&@nul-!heu_=)i8ywpoc9%5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
PIPELINE_ENABLED = False
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    BASE_DIR + '/templates',
)

MEDIA_ROOT = BASE_DIR + '/media'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'pipeline',
)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'statics'),)

PIPELINE_JS = {
    'stats': {
        'source_filenames': (
          'js/d3.js',
          'js/collections/*.js',
          'js/application.js',
        ),
        'output_filename': 'js/stats.js',
    },
    'components': {
        'source_filenames': (
          'components/jquery/dist/jquery.js',
          'components/bootstrap/dist/bootstrap.js',
        ),
        'output_filename': 'js/components.js',
    },
    'fileupload': {
        'source_filenames': (
            'components/jquery-cookie/jquery.cookie.js',
            'components/blueimp-file-upload/js/vendor/jquery.ui.widget.js',
            'components/blueimp-tmpl/js/tmpl.js',
            'components/blueimp-file-upload/js/jquery.fileupload.js',
            # 'components/blueimp-file-upload/js/jquery.fileupload-ui.js',
        ),
        'output_filename': 'js/fileupload.js',
    },
    'editablegrid': {
        'source_filenames': (
            'components/editablegrid/editablegrid.js',
            'components/editablegrid/editablegrid_renderers.js',
            'components/editablegrid/editablegrid_editors.js',
            'components/editablegrid/editablegrid_validators.js',
            'components/editablegrid/editablegrid_utils.js',
        ),
        'output_filename': 'css/editablegrid.js',
    },
}

PIPELINE_CSS = {
    'colors': {
        'source_filenames': (
          'css/core.css',
          'css/app.less',
          'css/colors/*.css',
          'css/layers.css'
        ),
        'output_filename': 'css/colors.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'components': {
        'source_filenames': (
            'components/bootstrap/dist/css/bootstrap.css',
            'components/bootstrap/dist/css/bootstrap-theme.css',
        ),
        'output_fileame': 'css/bootstrap.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'fileupload': {
        'source_filenames': (
            'components/blueimp-file-upload/css/jquery.fileupload.css',
            'components/blueimp-file-upload/css/jquery.fileupload-ui.css',
        ),
        'output_filename': "css/fileupload.css",
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'editablegrid': {
        'source_filenames': (
            'components/editablegrid/editablegrid.css',
        ),
        'output_filename': 'css/editablegrid.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATIC_ROOT = '/home/fangwei/sourceCode/jing/collectedstatic'

ROOT_URLCONF = 'fileupload.urls'

WSGI_APPLICATION = 'fileupload.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/statics-files/

STATIC_URL = '/statics/'
