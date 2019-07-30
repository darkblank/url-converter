from flask import request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.local import LocalProxy

from config import DevelopmentConfig


def get_engine(config_object_name):
    engine = create_engine(
        config_object_name.SQLALCHEMY_DATABASE_URI,
        pool_timeout=10,
    )
    return engine


# Todo: 동적으로 Config 불러올 수 있도록 수정
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=get_engine(DevelopmentConfig)))


def get_session():
    ctx = request._get_current_object()
    _session = Session()
    setattr(ctx, '_current_session', _session)  # app teardown 시 request ctx 에서 세션을 핸들링하기 위함
    return _session


session = LocalProxy(get_session)
