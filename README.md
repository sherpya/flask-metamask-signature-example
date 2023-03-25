# Flask and Metamask Wallet Signature Example

This is a simple example of how to connect a web3 wallet like Metamask
to a Flask backend, and verify the signature of a message signed by the wallet.

The backend is a Flask application that provides an API endpoint
for the frontend to request a message to sign,
and another API endpoint to verify the signature of the signed message.

The backend uses the `eth_account` library to recover the Ethereum address that signed the message,
and the `web3` library to connect to the Ethereum network.

The frontend is a simple HTML page with a button that triggers the signing process.
The frontend uses the `ethers` library to connect to the wallet and sign the message.

## Getting Started

To run this example, you will need Python 3.x installed on your system, as well as the following libraries:

- Flask
- web3
- eth_account

To install these libraries, you can run the following command:

`poetry install`

This will create a virtual environment and install all the dependencies specified in the `pyproject.toml` file.

Once you have installed the dependencies, you can start the backend by running the following command in your terminal:

`poetry run python app.py`

This will start the Flask server on `http://localhost:5000`.

To use the frontend, open the page in your web browser.

## Usage

1. Open the frontend in your web browser.
2. Click the "Ask the message and sign" button.
3. Metamask will ask you to connect your wallet. Connect your wallet if it is not already connected.
4. Metamask will display the message to sign. Click "Sign" to sign the message.
5. The frontend will send the signed message to the backend, which will verify the signature and return the result.
6. The frontend will display whether the signature was verified or not.

## License

This example is licensed under the MIT License. See the LICENSE file for details.
