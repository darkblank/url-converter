from flask_sqlalchemy_session import flask_scoped_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.local import LocalProxy

from config import DevelopmentConfig


def get_engine(config_object_name):
    engine = create_engine(
        config_object_name.SQLALCHEMY_DATABASE_URI,
        pool_timeout=10,
    )
    return engine


# Todo: 동적으로 Config 불러올 수 있도록 수정
Session = flask_scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=get_engine(DevelopmentConfig)))

session = LocalProxy(Session)
