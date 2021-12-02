from bottle import route, run, request, static_file
from json import dumps
import os

from conversion import *

PORT = os.environ.get("PORT")

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

    return static_file("index.html", root="./")

@route('/<filepath:re:.*\.png>')
def png(filepath):
    return static_file(filepath, root="./")

run(host='localhost', port=PORT, debug=True)