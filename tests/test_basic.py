import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    res = client.get('/')
    assert res.status_code == 200
    data = res.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'URL Shortener API'


def test_api_health(client):
    res = client.get('/api/health')
    assert res.status_code == 200
    data = res.get_json()
    assert data['status'] == 'ok'


def test_shorten_and_redirect(client):
    # Shorten a valid URL
    res = client.post('/api/shorten', json={'url': 'https://example.com'})
    assert res.status_code == 200
    data = res.get_json()
    assert 'short_code' in data
    short_code = data['short_code']

    # Redirect using the short code
    res = client.get(f'/{short_code}', follow_redirects=False)
    assert res.status_code == 302
    assert res.headers['Location'] == 'https://example.com'


def test_shorten_invalid_url(client):
    res = client.post('/api/shorten', json={'url': 'invalid-url'})
    assert res.status_code == 400
    data = res.get_json()
    assert 'error' in data


def test_stats_endpoint(client):
    # First create a shortened URL
    res = client.post('/api/shorten', json={'url': 'https://example.com'})
    short_code = res.get_json()['short_code']

    # Access redirect once to increment click count
    client.get(f'/{short_code}')

    # Get stats
    res = client.get(f'/api/stats/{short_code}')
    assert res.status_code == 200
    data = res.get_json()
    assert data['url'] == 'https://example.com'
    assert data['clicks'] >= 1
    assert 'created_at' in data


def test_stats_not_found(client):
    res = client.get('/api/stats/unknowncode')
    assert res.status_code == 404
