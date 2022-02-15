from googleapiclient.http import MediaFileUpload



def simple_test(drive_service):        
    results = drive_service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
        return
    print('Files:')
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))


def _create(service, file_name, media):
    file_metadata = {'name': file_name}
    file = service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
    print(file)

def image_create(drive_service, file_name):
    path = f"static/images/{file_name}"
    media = MediaFileUpload(path, mimetype='image/jpeg')
    _create(drive_service, file_name, media)



def audio_create(drive_service, file_name):
    path = f"static/audio/{file_name}"
    media = MediaFileUpload(path, mimetype='audio/*')
    _create(drive_service, file_name, media)


