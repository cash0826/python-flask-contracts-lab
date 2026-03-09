#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:id>')
def contract(id):
    # host = request.headers.get('Host')
    contract = next((c for c in contracts if c["id"] == id), None)
    if not any(contract["id"] == id for contract in contracts):
        return 'Not Found: you idiot', 404
    else:
        response_body = contract["contract_information"]
        status_code = 200
        headers = {}
        return make_response(response_body, status_code, headers)
  
@app.route('/customer/<string:customer_name>')
def customer(customer_name):
    if customer_name in customers:
        return '', 204
    else:
        return 'Not Found: you sucker', 404
      
if __name__ == '__main__':
    app.run(port=5555, debug=True)
