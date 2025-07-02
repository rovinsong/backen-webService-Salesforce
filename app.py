from flask import Flask, jsonify
from flask_cors import CORS  # 👈 Importar CORS
import requests
from salesforce_auth import get_salesforce_token

app = Flask(__name__)
CORS(app)  # 👈 Habilitar CORS

@app.route("/accounts", methods=["GET"])
def get_accounts():
    try:
        token, instance_url = get_salesforce_token()
        headers = {"Authorization": f"Bearer {token}"}
        url = f"{instance_url}/services/apexrest/AccountsAPI/"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        print("Error en /accounts:", e)
        return jsonify({"error": str(e)}), 500
