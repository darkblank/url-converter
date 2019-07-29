class Config:
    # Database
    SQLALCHEMY_DATABASE_URI = f'postgresql://<db_user>:<db_pwd>@localhost/<db_name>'
    # ETC
    SERVER_NAME = 'localhost:5000'
    DEBUG = False
    TESTING = False
    ENV = 'production'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://aiden:apfhd@localhost/dev_shortener'
    DEBUG = True
    ENV = 'development'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://aiden:apfhd@localhost/test_shortener'
    DEBUG = True
    TESTING = True
    ENV = 'test'
