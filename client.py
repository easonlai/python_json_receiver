import requests
import random

count = 0
while (count < 5):
    randomuuid = random.randrange(100)
    url = 'http://localhost:5000/api/add_message/' + str(randomuuid)
    res = requests.post(url, json={"name":"eason","phone":"+12345678","email":"eason@eason.com"})
    if res.ok:
        print(res.json())
    count = count + 1
print('End of post request')