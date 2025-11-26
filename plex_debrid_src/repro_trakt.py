import requests
import json

client_id = "0183a05ad97098d87287fe46da4ae286f434f32e8e951caad4cc147c947d79a3"
current_user = ["", ""]
session = requests.Session()

def post(url, data):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'Content-type': "application/json", "trakt-api-key": client_id, "trakt-api-version": "2"}
        
        print(f"DEBUG: current_user[1] is '{current_user[1]}'")
        if not current_user[1] == "":
            print("DEBUG: Adding Authorization header")
            headers["Authorization"] = "Bearer " + current_user[1]
        else:
            print("DEBUG: NOT adding Authorization header")
            
        print(f"DEBUG: Headers: {headers}")
        
        response = session.post(url, headers=headers, data=data)
        print(f"DEBUG: Status Code: {response.status_code}")
        print(f"DEBUG: Response Content: {response.text}")
        
    except Exception as e:
        print(f"DEBUG: Exception: {e}")

print("Testing Trakt OAuth Device Code...")
post('https://api.trakt.tv/oauth/device/code', json.dumps({'client_id': client_id}))
