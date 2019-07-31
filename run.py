import os

from app.app import create_app
from config import config_env_map

config_object = config_env_map[os.environ['APP_ENV']]

app = create_app(config_object)

if __name__ == '__main__':
    app.run()
