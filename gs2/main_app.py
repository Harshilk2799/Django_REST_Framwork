import json
import requests

URL = "http://127.0.0.1:8000/student_create/"

data = {
    "name": "Dharmesh",
    "roll":104,
    "city":"USA"
}

json_data = json.dumps(data)

res = requests.post(url=URL, data=json_data)

result = res.json()

print(result)