from app.app import create_app
from config import config_object

app = create_app(config_object)

if __name__ == '__main__':
    app.run()
