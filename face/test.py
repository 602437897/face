from aip import AipFace
import base64,auth,json,urllib,urllib2

APP_ID = '10440639'
API_KEY = 'REeeig5V9NpTkffDiqvTSyuV'
SECRET_KEY = 'oUdGrgbktr8G5BpirKwnqMdscGlGV3wu'

client = AipFace(APP_ID,API_KEY,SECRET_KEY)

content = auth.get_auth()
content = eval(content)
print content['access_token']
request_url = 'https://aip.baidubce.com/rest/2.0/face/v1/detect'
f = open('face.jpg', 'rb')
img = base64.b64encode(f.read())
print img
params = {"face_fields":"age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities","image":img,"max_face_num":5}
params = urllib.urlencode(params)
request_url = request_url + "?access_token=" + content['access_token']
request = urllib2.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib2.urlopen(request)
result = eval(response.read())
print('age:%s'%result['result'][0]['age'])
print('beauty:%s'%result['result'][0]['beauty'])
print('gender:%s'%result['result'][0]['gender'])
