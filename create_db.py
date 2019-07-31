from app.database import get_engine
from app.models import *
from config import config_object

if __name__ == '__main__':
    Base.metadata.create_all(bind=get_engine(config_object))
