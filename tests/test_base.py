def test_health_check(client):
    rv = client.get('/ping')
    assert rv.json and rv.json['ok'] == 'ok'
    assert 200 == rv.status_code
