
from flask import Flask, Response
from services.invoices import send_invoices

app = Flask(__name__)



@app.route("/invoices", methods=['POST'])
def handle_webhook():
    send_invoices()
    return Response(status=200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)