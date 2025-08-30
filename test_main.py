import os
import pytest
from unittest import mock
from unittest.mock import Mock, patch
from main import app as service_app

@pytest.fixture(scope="session", autouse=True)
def set_env():
    os.environ["private_key"] = "some_private_key"
    os.environ["stark_project_id"] = "0000"

@patch("common.provider.starkbank.Project")
def mock_starkbank():
    mock = Mock()
    return mock


@pytest.fixture
def client():
    service_app.config['TESTING'] = True # Enable testing mode
    with service_app.test_client() as client:
        yield client # Yield the client for use in tests

def test_request_invoice(client):
    with mock.patch('main.send_invoices') as mock_send_invoices:
        client.post('/invoices')
        assert mock_send_invoices.called
        
        