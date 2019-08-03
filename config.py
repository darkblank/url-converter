import os


class Config:
    # Database
    SQLALCHEMY_DATABASE_URI = 'postgresql://aiden:apfhd@localhost/dev_shortener'
    # ETC
    SERVER_NAME = 'localhost:5000'
    DEBUG = True
    TESTING = False
    ENV = 'production'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://aiden:apfhd@localhost/test_shortener'
    DEBUG = True
    TESTING = True
    ENV = 'test'


config_env_map = {
    'production': Config,
    'test': TestConfig,
}
