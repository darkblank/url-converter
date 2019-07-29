class Config:
    SERVER_NAME = 'localhost:5000'
    DEBUG = False
    TESTING = False
    ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    ENV = 'test'
