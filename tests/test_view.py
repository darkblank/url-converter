import uuid

import pytest

from app.models import Url


@pytest.fixture(scope='function')
def url(session):
    url = Url(
        id=str(uuid.uuid4()),
        original_url='https://naver.com',
        short_url='Hi',
    )
    session.add(url)
    session.commit()
    yield url
    session.query(Url).delete()
    session.commit()


def test_redirect_to_url(client, session, url):
    r = client.get(f'/{url.short_url}')
    renew = session.query(Url).filter(Url.short_url == url.short_url).first()
    assert r.status_code == 302
    assert renew.hit_count == url.hit_count + 1
    assert renew.last_used_at != url.last_used_at


def test_redirect_to_url_404(client):
    r = client.get(f'/doesNotExist')
    assert r.status_code == 404
    assert r.json['error'] == 'Url does not exist'
