from flask import Blueprint, request, jsonify
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

    if short_url and not Url.is_valid_url_format(short_url):
        return jsonify(error='short_url은 알파벳과 숫자로만 입력해 주세요'), 422

    obj = Url(original_url=original_url, short_url=short_url)
    try:
        session.add(obj)
        session.commit()
    except IntegrityError:
        return jsonify(error=f'{short_url}은 이미 존재하는 url입니다'), 409

    if not obj.short_url:
        obj.short_url = obj.generate_unique_shorten_url_from_pk()
        session.add(obj)
        session.commit()
    return jsonify(code='OK', data=dict(pk=obj.id, original_url=obj.original_url, short_url=obj.short_url))
