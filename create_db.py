from app.database import get_engine
from config import DevelopmentConfig
from app.models import *

if __name__ == '__main__':
    Base.metadata.create_all(bind=get_engine(DevelopmentConfig))  # Todo: 동적으로 Config 불러올 수 있도록 수정
