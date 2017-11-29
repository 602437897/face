import base64,base64,json,urllib,urllib2
from aip import AipFace
from VideoCapture import Device

APP_ID = '10440639'
API_KEY = 'REeeig5V9NpTkffDiqvTSyuV'
SECRET_KEY = 'oUdGrgbktr8G5BpirKwnqMdscGlGV3wu'

client = AipFace(APP_ID,API_KEY,SECRET_KEY)

def get_auth():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=REeeig5V9NpTkffDiqvTSyuV&client_secret=oUdGrgbktr8G5BpirKwnqMdscGlGV3wu'
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json;charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    return  eval(content)

def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()

def face_detect(filePath):
    options = {
        'max_face_num':5,
        'face_fields':'age,beauty,expression,faceshape'
    }
    result = client.detect(get_file_content(filePath),options)
    return result

def face_match(filePath):
    result = client.match([get_file_content('father.jpg'),get_file_content(filePath)])
    return result

def get_img(filePath = 'father.jpg'):
    cam = Device()
    cam.saveSnapshot(filePath)




