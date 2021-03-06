from bottle import route, run, request, static_file
from json import dumps
import os
import base64 

from conversion import *

@route('/upload', method='GET')
def upload_form():
    # An HTML form to upload a file
    return '''
    <form action="/sound_picture" method="post" enctype="multipart/form-data">
        <input type="file" name="data" />
        <input type="submit" value="Upload" />
    </form>
    '''

@route('/sound_picture', method='POST')
def sound_picture():
    request.files.get('data').save("./sound.mp3", overwrite=True)
    
    orig, avg, new = file_to_image("sound.mp3")

    orig.save("./orig.png")
    avg.save("./avg.png")
    new.save("./new.png")

    resp = {}

    with open('./orig.png', 'rb') as img:
        resp['orig'] = base64.b64encode(img.read()).decode('utf-8')

    with open('./avg.png', 'rb') as img:
        resp['avg'] = base64.b64encode(img.read()).decode('utf-8')
    
    with open('./new.png', 'rb') as img:
        resp['new'] = base64.b64encode(img.read()).decode('utf-8')
    
    return dumps(resp)



@route('/<filepath:re:.*\.png>')
def png(filepath):
    return static_file(filepath, root="./")

run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))