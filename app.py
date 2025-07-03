from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Usa tu token y URL aquí (reemplaza con variables de entorno si quieres)
ACCESS_TOKEN = 'Bearer 00DKZ000004eqNl!AQEAQHygJaxGanLIEvmDkzanvVTKE4lvW1F6DaW5pvrApHiwog9kycSXe.CAIU4J.HTcMGdnwdu3fJ3NnOrO8kUgOlBJuq_l'
INSTANCE_URL = 'https://ne1750098607375.my.salesforce.com'

@app.route('/accounts', methods=['GET'])
def get_accounts():
    query = "SELECT Id, Name,Razon_social__c,Type, Phone, Website FROM Account LIMIT 100"
    url = f"{INSTANCE_URL}/services/data/v60.0/query?q={query}"

    headers = {
        'Authorization': ACCESS_TOKEN,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
