from common.logger import logging
from common.provider import get_starkbank
from faker import Faker

fake = Faker('pt_BR')

def send_invoices():
    invoices_list = []
    starkbank = get_starkbank()
    for _ in range(9):
        invoices_list.append(
            starkbank.Invoice(
                amount=fake.random_number(digits=5),
                name=fake.name(),
                tax_id=fake.cpf()
            )
        )
    invoices_response = starkbank.invoice.create(invoices_list)
    for invoice in invoices_response:
        logging.info(invoice)