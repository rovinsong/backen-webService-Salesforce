import requests
import os

def get_salesforce_token():
    url = "https://welcome.salesforce.com/services/oauth2/token"
    payload = {
        'grant_type': 'password',
        'client_id': os.environ['CLIENT_ID'],
        'client_secret': os.environ['CLIENT_SECRET'],
        'username': os.environ['SF_USERNAME'],
        'password': os.environ['SF_PASSWORD'] + os.environ['SF_SECURITY_TOKEN']
    }

    response = requests.post(url, data=payload)
    response.raise_for_status()
    data = response.json()
    return data['access_token'], data['instance_url']
