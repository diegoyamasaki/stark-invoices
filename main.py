
from flask import Flask, request, Response
from faker import Faker
from configs import starkbank


app = Flask(__name__)
fake = Faker('pt_BR')


@app.route("/invoices", methods=['POST'])
def handle_webhook():
    invoices_list = []
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
        print(invoice)
    return Response(status=200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)