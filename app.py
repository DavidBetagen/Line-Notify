import requests

url = 'https://notify-api.line.me/api/notify'
token = 'JhexxaWsjUS1lxxxxx' # Line token
headers = {
     'content-type':'application/x-www-form-urlencoded',
     'Authorization':'Bearer ' + token
}

message = 'Hello World!! message form Mars'

response = requests.post(url, headers = headers, data = {'message': message})
print (response)