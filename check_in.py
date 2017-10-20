import requests
import json

data = {'message': 'Hello,  I  am  Liza'}
header = {'content-type': 'application/json'}

s = requests.post('http://cit-home1.herokuapp.com/api/register', data=json.dumps(data), headers=header)
print(s.status_code)
print(s.json())

s = requests.get('http://cit-home1.herokuapp.com/api/check_me')
print(s.json())
print(s.status_code)