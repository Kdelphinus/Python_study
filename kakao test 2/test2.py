import requests
import random

TOKEN = "a2e2b800925040e92b7e0cde0c1015e6"
BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"


def start():
    headers = {
        "X-Auth-Token": TOKEN,
        "Content-Type": "application/json",
    }

    data = '{ "problem": 2 }'

    response = requests.post(BASE_URL + "/start", headers=headers, data=data)

    return response.json().get("auth_key")


def location_data(auth_key):
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json",
    }

    response = requests.get(BASE_URL + "/locations", headers=headers)

    return response.json().get("locations")


def truck_data(auth_key):
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json",
    }

    response = requests.get(BASE_URL + "/trucks", headers=headers)

    return response.json().get("trucks")


def simulate(auth_key, commands):
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json",
    }

    data = f'{{ "commands": [ {commands} ] }}'

    response = requests.put(BASE_URL + "/simulate", headers=headers, data=data)
    print(response.json())
    return response.json().get("status")


def score(auth_key):
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json",
    }

    response = requests.get(BASE_URL + "/score", headers=headers)

    print(response.json().get("score"))


auth_key = start()
locations = location_data(auth_key)
truck = truck_data(auth_key)
status = "ready"


"""랜덤하게 배차 / score = 570.1105936220642 / failed_requests_count = 1860"""
while status == "ready":
    commands = ""
    for i in range(10):
        tmp = "[5, "
        for j in range(8):
            tmp += str(random.randrange(1, 5)) + ", "
        tmp += "6]"
        commands += f' {{ "truck_id": {i}, "command": {tmp}}} '
        if i < 9:
            commands += ","

    status = simulate(auth_key, commands)


"""배차 안함 / score = 596.4027149321267 / failed_requests_count = 1687"""
# while status == "ready":
#     commands = ""
#     status = simulate(auth_key, commands)

score(auth_key)
