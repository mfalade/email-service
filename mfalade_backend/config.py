import os

class Config(object):
    DEBUG = False
    TESTING = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('GMAIL_ADDY')
    MAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')


class DevelopmentConfiguration(Config):
    DEBUG = True


class TestingConfiguration(Config):
    TESTING = True


class ProductionConfiguration(Config):
    pass



app_config = dict(
    dev=DevelopmentConfiguration,
    production=ProductionConfiguration,
    test=TestingConfiguration
)
