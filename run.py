from app.app import create_app
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)  # Todo: 동적으로 Config 불러올 수 있도록 수정

if __name__ == '__main__':
    app.run()
