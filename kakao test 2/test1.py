from typing import SupportsComplex
import requests

TOKEN = "1d5f1764874aec88f4204feb38bd9206"
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

    return response.json().get("score")


def nothing(auth_key):  # score = 229.94747899159663, failed_requests_count = 351
    """배차 안함"""

    status = "ready"
    while status == "ready":
        commands = ""
        status = simulate(auth_key, commands)

    return score(auth_key)


def near(auth_key):  # score = 223.10818977591038, failed_requests_count = 316
    """근처에서 자전거가 가장 적은 곳에 배치"""

    status = "ready"
    commands = '{ "truck_id": 0, "command": [2, 1]}, { "truck_id": 1, "command": [2, 2, 2, 1]}, { "truck_id": 2, "command": [1, 1, 1, 2, 2, 2]}, { "truck_id": 3, "command": [1, 1, 1, 2]}, { "truck_id": 4, "command": [1, 1, 2, 2]}'
    simulate(auth_key, commands)
    while status == "ready":
        locations = location_data(auth_key)
        truck = truck_data(auth_key)
        commands = ""
        for i in range(5):
            command = "["
            now = truck[i].get("location_id")  # 현재 트럭 위치
            loaded_nums = truck[i].get("loaded_bikes_count")  # 트럭이 가지고 있는 자전거 수
            now_bikes_nums = locations[now].get("located_bikes_count")  # 현재 정거장의 자전거 수
            idx = 0
            flag = False
            while idx < 10:

                if flag:
                    min_num = 101
                    min_next_spot = 0
                    dn = 0
                    if (
                        now + 1 < 25
                        and locations[now + 1].get("located_bikes_count") < min_num
                    ):  # 위
                        min_num = locations[now + 1].get("located_bikes_count")
                        next_spot = 1
                        dn = 1
                    if (
                        now + 5 < 25
                        and locations[now + 5].get("located_bikes_count") < min_num
                    ):  # 오른쪽
                        min_num = locations[now + 5].get("located_bikes_count")
                        next_spot = 2
                        dn = 5
                    if (
                        now - 1 > -1
                        and locations[now - 1].get("located_bikes_count") < min_num
                    ):  # 아래
                        min_num = locations[now - 1].get("located_bikes_count")
                        next_spot = 3
                        dn = -1
                    if (
                        now - 5 > -1
                        and locations[now - 5].get("located_bikes_count") < min_num
                    ):  # 왼쪽
                        min_num = locations[now - 5].get("located_bikes_count")
                        next_spot = 4
                        dn = -5

                    now += dn
                    if idx == 9:
                        command += f"{next_spot}]"
                    else:
                        command += f"{next_spot}, "
                    idx += 1
                    flag = False
                else:
                    while idx < 10 and now_bikes_nums < 3 and loaded_nums:
                        loaded_nums -= 1
                        now_bikes_nums += 1
                        idx += 1
                        if idx == 10:
                            command += "6]"
                            break
                        command += "6, "
                    while idx < 10 and now_bikes_nums > 3:
                        loaded_nums += 1
                        now_bikes_nums -= 1
                        idx += 1
                        if idx == 10:
                            command += "5]"
                            break
                        command += "5, "
                    locations[now]["located_bikes_count"] = now_bikes_nums
                    flag = True

            commands += f' {{ "truck_id": {i}, "command": {command}}} '
            if i < 4:
                commands += ","

        status = simulate(auth_key, commands)

    return score(auth_key)


def route_setting(auth_key):  # score = 246.44743347338937, failed_requests_count = 219
    """트럭의 루트를 정하여 배차, 5번차는 12번만 관리"""
    status = "ready"
    commands = '{ "truck_id": 0, "command": [2, 1]}, { "truck_id": 1, "command": [2, 2, 2, 1]}, { "truck_id": 2, "command": [1, 1, 1, 2, 2, 2]}, { "truck_id": 3, "command": [1, 1, 1, 2]}, { "truck_id": 4, "command": [1, 1, 2, 2]}'
    simulate(auth_key, commands)
    route = [
        [6, 1, 0, 5, 10, 11],
        [16, 17, 22, 21, 20, 15],
        [18, 23, 24, 19, 14, 13],
        [8, 7, 2, 3, 4, 9],
    ]

    while status == "ready":
        locations = location_data(auth_key)
        truck = truck_data(auth_key)
        commands = ""

        for i in range(5):
            if i < 4:
                command = "["
                now = truck[i].get("location_id")  # 현재 트럭 위치
                idx = 0
                while idx < 10:
                    tmp = route[i].index(now)
                    if tmp < 5:
                        diff = route[i][tmp + 1] - route[i][tmp]
                    else:
                        diff = route[i][0] - route[i][tmp]
                    now += diff

                    if diff == 1:
                        command += "1, "
                    elif diff == 5:
                        command += "2, "
                    elif diff == -1:
                        command += "3, "
                    else:
                        command += "4, "
                    idx += 1

                    if locations[now].get("located_bikes_count") > 3:
                        command += "5, "
                    elif locations[now].get("located_bikes_count") < 3:
                        command += "6, "
                    else:
                        continue
                    idx += 1

                command = command[:-2] + "]"
                commands += f' {{ "truck_id": {i}, "command": {command}}}, '
            else:
                if locations[now].get("located_bikes_count") < 3:
                    if locations[now - 5].get("located_bikes_count") > 3:
                        command = "[4, 5, 2, 6]"
                    elif locations[now - 1].get("located_bikes_count") > 3:
                        command = "[3, 5, 3, 6]"
                    elif locations[now + 5].get("located_bikes_count") > 3:
                        command = "[2, 5, 4, 6]"
                    elif locations[now + 1].get("located_bikes_count") > 3:
                        command = "[1, 5, 3, 6]"
                elif locations[now].get("located_bikes_count") > 3:
                    if locations[now - 5].get("located_bikes_count") < 3:
                        command = "[5, 4, 6, 2]"
                    elif locations[now - 1].get("located_bikes_count") < 3:
                        command = "[5, 3, 6, 3]"
                    elif locations[now + 5].get("located_bikes_count") < 3:
                        command = "[5, 2, 6, 4]"
                    elif locations[now + 1].get("located_bikes_count") < 3:
                        command = "[5, 1, 6, 3]"
                commands += f' {{ "truck_id": {i}, "command": {command}}} '

        status = simulate(auth_key, commands)

    return score(auth_key)


def route_another(auth_key):  # 여러 조건으로 실행한 것들이 있음
    """
    * 4번차가 12번을 기준으로 밑으로 한 바퀴 도는 루트
    score = 250.31111694677872, failed_requests_count = 200

    * 4번차가 12번을 기준으로 위로 한 바퀴 도는 루트
    score = 249.72029411764706, failed_requests_count = 203

    * 4번차가 전체를 도는 루트
    score = 248.17282212885155, failed_requests_count = 211

    """
    status = "ready"
    # 4번차가 일부만 돌 때
    commands = '{ "truck_id": 0, "command": [2, 1]}, { "truck_id": 1, "command": [2, 2, 2, 1]}, { "truck_id": 2, "command": [1, 1, 1, 2, 2, 2]}, { "truck_id": 3, "command": [1, 1, 1, 2]}, { "truck_id": 4, "command": [1, 1, 2, 2]}'

    # 4번차가 전체를 도는 루트일 때
    # commands = '{ "truck_id": 0, "command": [2, 1]}, { "truck_id": 1, "command": [2, 2, 2, 1]}, { "truck_id": 2, "command": [1, 1, 1, 2, 2, 2]}, { "truck_id": 3, "command": [1, 1, 1, 2]}'
    simulate(auth_key, commands)

    # 4번차가 12번을 기준으로 밑으로 한 바퀴 도는 루트
    route = [
        [6, 1, 0, 5, 10, 11],
        [16, 17, 22, 21, 20, 15],
        [18, 23, 24, 19, 14, 13],
        [8, 7, 2, 3, 4, 9],
        [12, 7, 6, 11, 16, 17],
    ]

    # 4번차가 12번을 기준으로 위로 한 바퀴 도는 루트
    # route = [
    #     [6, 1, 0, 5, 10, 11],
    #     [16, 17, 22, 21, 20, 15],
    #     [18, 23, 24, 19, 14, 13],
    #     [8, 7, 2, 3, 4, 9],
    #     [12, 7, 8, 13, 18, 17],
    # ]

    # 4번차가 전체를 도는 루트
    # route = [
    #     [6, 1, 0, 5, 10, 11],
    #     [16, 17, 22, 21, 20, 15],
    #     [18, 23, 24, 19, 14, 13],
    #     [8, 7, 2, 3, 4, 9],
    #     [
    #         0,
    #         5,
    #         10,
    #         15,
    #         20,
    #         21,
    #         16,
    #         11,
    #         6,
    #         1,
    #         2,
    #         7,
    #         12,
    #         17,
    #         22,
    #         23,
    #         18,
    #         13,
    #         8,
    #         3,
    #         4,
    #         9,
    #         14,
    #         19,
    #         24,
    #         23,
    #         18,
    #         13,
    #         8,
    #         3,
    #         2,
    #         7,
    #         12,
    #         17,
    #         22,
    #         21,
    #         16,
    #         11,
    #         6,
    #         1,
    #     ],
    # ]

    while status == "ready":
        locations = location_data(auth_key)
        truck = truck_data(auth_key)
        commands = ""

        for i in range(5):
            command = "["
            now = truck[i].get("location_id")  # 현재 트럭 위치
            idx = 0
            while idx < 10:
                tmp = route[i].index(now)
                if tmp < len(route[i]) - 1:
                    diff = route[i][tmp + 1] - route[i][tmp]
                else:
                    diff = route[i][0] - route[i][tmp]
                now += diff

                if diff == 1:
                    command += "1, "
                elif diff == 5:
                    command += "2, "
                elif diff == -1:
                    command += "3, "
                else:
                    command += "4, "
                idx += 1

                if locations[now].get("located_bikes_count") > 3:
                    command += "5, "
                elif locations[now].get("located_bikes_count") < 3:
                    command += "6, "
                else:
                    continue
                idx += 1

            command = command[:-2] + "]"
            commands += f' {{ "truck_id": {i}, "command": {command}}} '
            if i < 4:
                commands += ","

        status = simulate(auth_key, commands)

    return score(auth_key)


auth_key = start()
# print("nothing:", nothing(auth_key))
# print("near:", near(auth_key))
# print("route_setting:", route_setting(auth_key))
print("route_another:", route_another(auth_key))
