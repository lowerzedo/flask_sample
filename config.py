import os


# Enable debug mode, that will refresh the page when you make changes.
APP_ENV = os.environ.get('STAGE', 'dev')

class Config(object):
    SECRET_KEY = "foo"