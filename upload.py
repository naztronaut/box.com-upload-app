import requests as requests
import generate_jwt


def upload_file(file):
    print('upload.py')
    API_ENDPOINT = "https://upload.box.com/api/2.0/files/content"
    token = generate_jwt.get_key()

    HEADERS = {"authorization": "Bearer " + token, "as-user": "12687310242"}

    r = requests.post(url=API_ENDPOINT, headers=HEADERS, data={'attributes': '{"name":"' + file.filename + '", "parent":{"id":"112221918845"}}'}, files={'file': file.read()})
    print(r.json())
    return r.json()
