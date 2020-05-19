from boxsdk import JWTAuth, Client

# Get config.json from box.com dev console
config = JWTAuth.from_settings_file('config.json')

client = Client(config)

user_to_impersonate = client.user(user_id='12687310242')
user_client = client.as_user(user_to_impersonate)

def upload_large_file(file, size):
    print("sdk_jwt")
    file_size = size
    upload_session = client.as_user(user_to_impersonate).folder('112221918845').create_upload_session(file_size, file.filename)
    print('Created upload session {0} with chunk size of {1} bytes'.format(upload_session.id, upload_session.part_size))

    chunked_uploader = upload_session.get_chunked_uploader(file, file_size)
    uploaded_file = chunked_uploader.start()
    print('File "{0}" uploaded to Box with file ID {1}'.format(uploaded_file.name, uploaded_file.id))
    print(uploaded_file)
    return "done"

    # To commit the file - looks like it's not needed
    # print(chunked_uploader)
    # sha1 = hashlib.sha1()
    # file_attributes = {
    #     "description": "File has been uploaded via Chunked Upload"
    # }
    # upload_session = client.upload_session(upload_session.id)
    # uploaded_file = upload_session.commit(sha1.digest(), file_attributes=file_attributes)
    # print('Successfully uploaded file {0} with description {1}'.format(uploaded_file.id, uploaded_file.description))



def upload_file(file, size):
    print(type(file))
    print(size)
    print(len(file.read()))
    folder_id = '112221918845'
    new_file = client.as_user(user_to_impersonate).folder(folder_id).upload(file)
    print('File "{0}" uploaded to Box with file ID {1}'.format(new_file.name, new_file.id))
    return 'uploaded'
