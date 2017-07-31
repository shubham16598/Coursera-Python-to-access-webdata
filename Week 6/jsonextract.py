import urllib.request as ur
import json

# json_url = 'http://python-data.dr-chuck.net/comments_42.json'

json_url = input("Enter location: ")
print("Retrieving ", json_url)
data = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')

info = json.loads(data)
sum = 0
for comment in info["comments"]:
    sum += int(comment["count"])
print (sum)
