import requests
import random

TOKEN = "a2e2b800925040e92b7e0cde0c1015e6"
BASE_URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"


def start():
    headers = {
        "X-Auth-Token": TOKEN,
        "Content-Type": "application/json",
    }

    data = '{ "problem": 1 }'

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
commands = '{ "truck_id": 1, "command": [2, 2, 2, 2]}, { "truck_id": 2, "command": [1, 1, 1, 2, 2, 2]}, { "truck_id": 3, "command": [1, 1, 1]}, { "truck_id": 4, "command": [1, 1, 2, 2]}'
simulate(auth_key, commands)


"""랜덤하게 배차 / score = 227.15735994397758 / failed_requests_count = 317"""
while status == "ready":
    commands = ""
    for i in range(5):
        tmp = "[5"
        for j in range(10):
            tmp += str(random.randrange(1, 7)) + ", "
        tmp += "6]"
        commands += f' {{ "truck_id": {i}, "command": {tmp}}} '
        if i < 4:
            commands += ","
    status = simulate(auth_key, commands)


"""배차 안함 / score = 229.94747899159663 / failed_requests_count = 351"""
# while status == "ready":
#     commands = ""
#     status = simulate(auth_key, commands)


"""랜덤 + 배차 / score = 197.5891281512605 / failed_requests_count = 460"""
while status == "ready":
    locations = location_data(auth_key)
    truck = truck_data(auth_key)
    commands = ""

    for i in range(5):
        command = "["
        now = truck[i].get("location_id")  # 현재 트럭 위치
        loaded_nums = truck[i].get("loaded_bikes_count")  # 트럭이 가지고 있는 자전거 수
        idx = 0
        flag = False

        while idx < 10:
            now_bikes_nums = locations[now].get("located_bikes_count")  # 현재 정거장의 자전거 수
            if flag:
                next_spot = random.randrange(1, 5)
                if idx == 9:
                    command += f"{next_spot}]"
                else:
                    command += f"{next_spot}, "
                idx += 1
                flag = False
            else:
                while now_bikes_nums < 3 and loaded_nums:
                    loaded_nums -= 1
                    idx += 1
                    if idx == 10:
                        command += "6]"
                        break
                    command += "6, "
                if now_bikes_nums > 3:
                    if idx == 9:
                        command += "5]"
                    else:
                        command += "5, "
                    loaded_nums += 1
                    idx += 1
                flag = True

        commands += f' {{ "truck_id": {i}, "command": {command}}} '
        if i < 4:
            commands += ","

    status = simulate(auth_key, commands)


"""구역을 나누고 개수를 파악하여 배차 / score = 226.34543767507003 / failed_requests_count = 339"""
# while status == "ready":
#     locations = location_data(auth_key)
#     truck = truck_data(auth_key)
#     commands = ""
#     areas = [
#         [0, 1, 2, 5, 6, 7, 10, 11, 12],
#         [10, 11, 12, 15, 16, 17, 20, 21, 22],
#         [12, 13, 14, 17, 18, 19, 22, 23, 24],
#         [2, 3, 4, 7, 8, 9, 12, 13, 14],
#         [6, 7, 8, 11, 12, 13, 16, 17, 18],
#     ]
#     for i in range(5):
#         command = "["
#         now = truck[i].get("location_id")  # 현재 트럭 위치
#         loaded_nums = truck[i].get("loaded_bikes_count")  # 트럭이 가지고 있는 자전거 수
#         area = areas[i]
#         idx = 0
#         flag = False

#         while idx < 10:
#             now_bikes_nums = locations[now].get("located_bikes_count")  # 현재 정거장의 자전거 수
#             if flag:
#                 min_num = 101
#                 next_spot = 0
#                 dn = 0

#                 if (
#                     now - 1 in area
#                     and locations[now - 1].get("located_bikes_count") < min_num
#                 ):  # 아래
#                     min_num = locations[now - 1].get("located_bikes_count")
#                     next_spot = 3
#                     dn = -1
#                 if (
#                     now + 1 in area
#                     and locations[now + 1].get("located_bikes_count") < min_num
#                 ):  # 위
#                     min_num = locations[now + 1].get("located_bikes_count")
#                     next_spot = 1
#                     dn = 1
#                 if (
#                     now - 5 in area
#                     and locations[now - 5].get("located_bikes_count") < min_num
#                 ):  # 왼쪽
#                     min_num = locations[now - 5].get("located_bikes_count")
#                     next_spot = 4
#                     dn = -5
#                 if (
#                     now + 5 in area
#                     and locations[now + 5].get("located_bikes_count") < min_num
#                 ):  # 오른쪽
#                     min_num = locations[now + 5].get("located_bikes_count")
#                     next_spot = 2
#                     dn = 5

#                 now += dn
#                 if idx == 9:
#                     command += f"{next_spot}]"
#                 else:
#                     command += f"{next_spot}, "
#                 idx += 1
#                 flag = False
#             else:
#                 while idx < 10 and now_bikes_nums < 3 and loaded_nums:
#                     command += "6, "
#                     loaded_nums -= 1
#                     locations[now]["located_bikes_count"] += 1
#                     idx += 1
#                 if now_bikes_nums > 3:
#                     command += "5, "
#                     loaded_nums += 1
#                     locations[now]["located_bikes_count"] -= 1
#                     idx += 1
#                 flag = True

#         commands += f' {{ "truck_id": {i}, "command": {command}}} '
#         if i < 4:
#             commands += ","

#     status = simulate(auth_key, commands)


score(auth_key)
