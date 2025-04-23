import pytest

from hello import pancakes


@pytest.fixture
def client():
	return pancakes.test_client()


def test_put_any_name_here(client):
	response = client.get('/hello')
	assert response.status_code == 200
	#assert response.data == {"message": "Hello, World!"}
	assert response.json == {"message": "Hello, World!"}
	




