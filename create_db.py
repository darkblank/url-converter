import os

from app.database import get_engine
from app.models import *
from config import config_env_map

config_object = config_env_map[os.environ['APP_ENV']]

if __name__ == '__main__':
    Base.metadata.create_all(bind=get_engine(config_object))
