# main.py
from flask import Flask, jsonify
import requests
from salesforce_auth import get_salesforce_token

app = Flask(__name__)

@app.route("/accounts", methods=["GET"])
def get_accounts():
    token, instance_url = get_salesforce_token()
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{instance_url}/services/apexrest/AccountsAPI/"
    response = requests.get(url, headers=headers)
    return jsonify(response.json())
