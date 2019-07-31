from flask import Blueprint, request, jsonify
from sqlalchemy import exists
from sqlalchemy.exc import IntegrityError

from app.database import session
from app.models import Url

api = Blueprint('api', __name__)


@api.route('/urls', methods=['POST'])
def create_short_url():
    data = request.get_json()
    original_url = data.get('original_url')
    short_url = data.get('short_url')

    if not original_url:
        return jsonify(error='original url을 입력해 주세요'), 412

    if short_url:
        if not Url.is_valid_url_format(short_url):
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
