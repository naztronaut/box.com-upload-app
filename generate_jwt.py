import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
import json
import time
import secrets


def get_key():
    # Get config.json from box.com dev console
    config = json.load(open('config.json'))

    appAuth = config["boxAppSettings"]["appAuth"]
    privateKey = appAuth["privateKey"]
    passphrase = appAuth["passphrase"]

    # https://cryptography.io/en/latest/
    key = load_pem_private_key(
      data=privateKey.encode('utf8'),
      password=passphrase.encode('utf8'),
      backend=default_backend(),
    )

    authentication_url = 'https://api.box.com/oauth2/token'

    claims = {
      'iss': config['boxAppSettings']['clientID'],
      'sub': config['enterpriseID'],
      'box_sub_type': 'enterprise',
      'aud': authentication_url,
      'jti': secrets.token_hex(64),
      'exp': round(time.time()) + 45
    }

    keyId = config['boxAppSettings']['appAuth']['publicKeyID']

    assertion = jwt.encode(
      claims,
      key,
      algorithm='RS512',
      headers={
        'kid': keyId
      }
    )

    params = urlencode({
      'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
      'assertion': assertion,
      'client_id': config['boxAppSettings']['clientID'],
      'client_secret': config['boxAppSettings']['clientSecret']
    }).encode()

    request = Request(authentication_url, params)
    response = urlopen(request).read()
    access_token = json.loads(response)['access_token']

    return access_token
    # print(access_token)
