from unittest import mock
from services.invoices import send_invoices

def test_send_invoices():
    with mock.patch('services.invoices.get_starkbank') as mock_get_starkbank:
        send_invoices()
        assert mock_get_starkbank.return_value.Invoice.called
        assert mock_get_starkbank.return_value.invoice.create.called