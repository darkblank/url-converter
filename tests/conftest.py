import os

import pytest

from app.app import create_app
from app.database import get_engine
from app.models import Base
from config import config_env_map


@pytest.fixture(scope='session')
def app():
    env = os.environ['APP_ENV']
    if env != 'test':
        raise EnvironmentError('must set "APP_ENV" env to "test"')
    config_object = config_env_map[env]

    app = create_app(config_object)
    engine = get_engine(config_object)
    metadata = Base.metadata
    metadata.create_all(bind=engine)
    yield app
    metadata.drop_all(bind=engine)


@pytest.fixture(scope='function')
def client(app):
    with app.test_client() as client:
        yield client
