import datetime
import string
from random import choice

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

    def generate_unique_shorten_url(self):
        chars = string.ascii_letters + string.digits
        n = self.id
        url = ''
        while n:
            n, r = divmod(n, len(chars))
            url += chars[r]
        return url
