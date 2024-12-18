from dotenv import load_dotenv
import os
from requests import post,get
import base64
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(client_id,client_secret)

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization':'Basic '+ auth_base64,
        'Content-Type':'application/x-www-form-urlencoded'
    }
    data = {"grant_type":"client_credentials"}
    result = post(url,headers=headers,data=data)

    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

#token = get_token()
#print(token)

def get_auth_header(token):
    return {'Authorization':'Bearer ' + token}

def search_for_artist(token,artist_name):
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f'?q={artist_name}&type=artist&limit=1'

    query_url = url + query
    result = get(query_url,headers=headers)
    result_json = json.loads(result.content)['artists']['items']

    if len(result_json)==0:
        print("No artist with this record exists....")
        return None
    
    result_json[0]

token = get_token()
#print(token)
result=search_for_artist(token,"Burna Boy")
print(result['name'])