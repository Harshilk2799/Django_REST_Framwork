import json
import requests

URL = "http://127.0.0.1:8000/studentapi/"


def get_data(id = None):
    data = {}
    if id is not None:
        data = {"id": id}
    
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# get_data(2)



def post_data():
    data = {
        "name":"Bharat",
        "roll":103,
        "city":"Vejalpur"
    }
    json_data = json.dumps(data)
    response = requests.post(url=URL, data=json_data)
    data = response.json()
    print(data)

# post_data()


def update_data_partialy():
    data = {
        "id": 3,
        "city":"Vejalpur-Ahmedabad"
    }
    json_data = json.dumps(data)
    response = requests.patch(url=URL, data=json_data)
    data = response.json()
    print(data)

# update_data_partialy()


def update_data_fully():
    data = {
        "id": 3,
        "name": "Bharat",
        "roll":103,
        "city":"Vejalpur/Ahmedabad"
    }
    json_data = json.dumps(data)
    response = requests.put(url=URL, data=json_data)
    data = response.json()
    print(data)

# update_data_fully()

def delete_data():
    data = {
        "id": 2,
    }
    json_data = json.dumps(data)
    response = requests.delete(url=URL, data=json_data)
    data = response.json()
    print(data)

delete_data()