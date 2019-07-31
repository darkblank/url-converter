from app.models import Url


def test_create_short_url_without_custom_url(client):
    original_url = 'http://www.naver.com'
    r = client.post('api/urls', json=dict(original_url=original_url))
    assert r.status_code == 200
    assert r.json['data']['original_url'] == original_url


def test_create_short_url_with_custom_url(client):
    original_url = 'https://www.naver.com'
    short_url = 'shortUrl'
    r = client.post('api/urls', json=dict(original_url=original_url, short_url=short_url))
    assert r.status_code == 200
    assert r.json['data']['short_url'] == short_url


def test_get_urls(client, session):
    r = client.get('api/urls')
    assert r.status_code == 200
    assert len(r.json['data']) == session.query(Url).count()


def test_create_short_url_aleady_exists(client):
    original_url = 'https://www.naver.com'
    short_url = 'shortUrl'
    r = client.post('api/urls', json=dict(original_url=original_url, short_url=short_url))
    assert r.status_code == 409
    assert r.json['error'] == f'{short_url}은 이미 존재하는 url입니다'


def test_create_short_url_with_invalid_custom_url(client):
    original_url = 'https://www.naver.com'
    short_url = 'short_url'
    r = client.post('api/urls', json=dict(original_url=original_url, short_url=short_url))
    assert r.status_code == 422
    assert r.json['error'] == 'short_url은 알파벳과 숫자로만 입력해 주세요'



