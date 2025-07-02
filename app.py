from flask import Flask, request, jsonify, redirect
import requests
import os

app = Flask(__name__)

@app.route("/oauth/callback")
def oauth_callback():
    code = request.args.get('code')
    if not code:
        return jsonify({'error': 'Missing authorization code'}), 400

    token_url = "https://login.salesforce.com/services/oauth2/token"
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': os.environ['CLIENT_ID'],
        'client_secret': os.environ['CLIENT_SECRET'],
        'redirect_uri': 'https://backen-webservice-salesforce.onrender.com/oauth/callback'
    }

    response = requests.post(token_url, data=payload)
    if response.status_code != 200:
        return jsonify({'error': 'Failed to get access token', 'details': response.text}), 500

    token_data = response.json()
    # Guarda el token en sesión o DB si lo deseas
    return jsonify(token_data)
