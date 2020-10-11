import os

from base64 import b64decode

secret = b64decode( os.urandom(32)).decode('utf-8')

class Config:
    SECRET_KEY = secret
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev = DevelopmentConfig,
    test = TestingConfig,
    prod = ProductionConfig
)