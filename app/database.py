import os

from flask import request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.local import LocalProxy

from config import config_env_map

config_object = config_env_map[os.environ['APP_ENV']]


def get_engine(config_object_name):
    engine = create_engine(
        config_object_name.SQLALCHEMY_DATABASE_URI,
        pool_timeout=10,
    )
    return engine


Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=get_engine(config_object)))


def get_session():
    ctx = request._get_current_object()
    _session = Session()
    setattr(ctx, '_current_session', _session)  # app teardown 시 request ctx 에서 세션을 핸들링하기 위함
    return _session


session = LocalProxy(get_session)
