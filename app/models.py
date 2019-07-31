import datetime
import random
import re
import string

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

__all__ = ['Base', 'Url']

Base = declarative_base()


class Url(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    original_url = Column(String(255), nullable=False)
    short_url = Column(String(30), nullable=True, unique=True)
    hit_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_used_at = Column(DateTime, nullable=True)

    @staticmethod
    def is_valid_url_format(url):
        pattern = re.compile('^[A-Za-z0-9]+$')
        return bool(pattern.match(url))

    @staticmethod
    def generate_random_str(length=5):
        chars = string.ascii_letters + string.digits
        return ''.join((random.choice(chars) for x in range(length)))
