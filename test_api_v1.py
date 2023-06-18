import json
import pytest
from flask import Flask

from application import application


@pytest.fixture
def client():
    application.config['TESTING'] = True
    with application.test_client() as client:
        yield client


def test_get_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert len(response.json) == 4  # Assuming 3 products are initially present

'''
def test_add_product(client):
    new_product = {
        "name": "New Product",
        "description": "Test Description",
        "price": 2.5,
        "tax": 0.1
    }

    response = client.post('/products', json=new_product)
    assert response.status_code == 201

    # Verify the product was added correctly
    assert response.json['id'] == 4  # Assuming the next ID is 4
    assert len(response.json.keys()) == 6  # Assuming no extra keys are added

    # Verify the new product is in the list
    response = client.get('/products')
    assert response.status_code == 200
    assert len(response.json) == 4  # Assuming there are now 4 products


def test_add_product_invalid_request(client):
    response = client.post('/products', data=json.dumps({"invalid": "data"}), content_type='application/json')
    assert response.status_code == 415
    assert response.json['error'] == 'Request must be JSON'
'''    
    
