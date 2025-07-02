from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import requests
from salesforce_auth import get_salesforce_token

app = Flask(__name__)
CORS(app)

@app.route("/oauth/callback")
def oauth_callback():
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "Missing authorization code"}), 400
    return jsonify({"code": code})
