import requests
import json

def istek():

    r = requests.get('https://reqres.in/api/users', allow_redirects=False)
    bilgi = {"page": 2}
    response_get = requests.get(r, params=bilgi)

    print(r.status_code)

istek()

