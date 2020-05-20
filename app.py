from flask import Flask, request, jsonify
import upload as uf
import sdk_jwt as sj

app = Flask(__name__, static_folder='./ui/build', static_url_path='/')


# Serve React app
# TODO: Place react app files in this repo and put build/ dir in .gitignore
@app.route('/')
def main():
    return app.send_static_file('index.html')


# Upload - looks at the content length - if less than 30 MB, use the simple upload, otherwise use sdk chunk uploader
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.files:
        file = request.files['uploaded']
        if request.content_length < 30000000:
            resp = uf.upload_file(file)
        else:
            file_size = len(file.read())
            file.stream.seek(0)
            resp = sj.upload_large_file(file, file_size)
    #TODO: clean up response - doesn't do any error handling
    return resp

