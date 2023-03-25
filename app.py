#!/usr/bin/env python3
import uuid

from eth_account.messages import encode_defunct
from flask import Flask, render_template, request, jsonify
from web3 import Web3
from web3.auto import w3
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
# Fake storage
messages = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/message/<string:address>')
def get_message(address):
    address = Web3.to_checksum_address(address)
    message = f'''This message is required to connect your wallet {address} to your account.

Nonce:
{uuid.uuid4()}'''
    # generate otp
    messages[address] = message
    return jsonify({'message': message})


@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    address = Web3.to_checksum_address(data.get('address'))
    signature = data.get('signature')

    if not address or not signature:
        raise BadRequest('Invalid address or signature')

    message = messages.get(address)
    if not message:
        raise BadRequest('Message for address not found')

    encoded = encode_defunct(text=message)
    signed_address = w3.eth.account.recover_message(encoded, signature=signature)
    is_verified = signed_address == address

    if is_verified:
        # TODO: save the address in the account
        # remove otp
        messages.pop(address)

    return jsonify({'status': 'success' if is_verified else 'error'})


if __name__ == '__main__':
    app.run(debug=True)
