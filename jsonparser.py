import urllib.request
import json

url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyDKXPuaXh84T_tVVQcxQdbQS8TzNk2uuuU%20&cx=017576662512468239146:omuauf_lfve&q=facebok"
response = urllib.request.urlopen(url)
content = response.read()
data = json.loads(content.decode("utf8"))

#for i in data['items']:
#    print(i['link'])

print(data)