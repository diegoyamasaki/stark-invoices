from unittest import mock
from common.provider import get_starkbank

def test_get_starkbank():
    with mock.patch('common.provider.starkbank') as mock_starkbank:
        get_starkbank()
        assert mock_starkbank.user