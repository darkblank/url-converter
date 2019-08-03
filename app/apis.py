from flask import Blueprint, request, jsonify
from sqlalchemy import exists

from app.database import session
from app.models import Url
from utils import date_to_str

api = Blueprint('api', __name__)


@api.route('/urls', methods=['GET'])
def get_urls():
    urls = session.query(Url).all()
    return jsonify(
        code='OK',
        data=[dict(
            pk=url.id,
            original_url=url.original_url,
            short_url=url.short_url,
            hit_count=url.hit_count,
            created_at=date_to_str(url.created_at),
            last_used_at=date_to_str(url.last_used_at),
        ) for url in urls]
    )


@api.route('/urls', methods=['POST'])
def create_short_url():
    data = request.get_json()
    original_url = data.get('original_url')
    short_url = data.get('short_url')

    if not original_url:
        return jsonify(error='original url을 입력해 주세요'), 400

    if not Url.is_valid_original_url_format(original_url):
        return jsonify(error='올바른 형식의 original_url을 입력해 주세요'), 422

    if short_url:
        if not Url.is_valid_short_url(short_url):
            return jsonify(error='short_url은 알파벳과 숫자로만 입력해 주세요'), 422
        if session.query(exists().where(Url.short_url == short_url)).scalar():
            return jsonify(error=f'{short_url}은 이미 존재하는 url입니다'), 409
    else:
        while True:
            short_url = Url.generate_random_str()
            if not session.query(exists().where(Url.short_url == short_url)).scalar():
                break

    obj = Url(original_url=original_url, short_url=short_url)
    session.add(obj)
    session.commit()

    return jsonify(code='OK', data=dict(pk=obj.id, original_url=obj.original_url, short_url=obj.short_url))
