import requests

TOKEN = "1d5f1764874aec88f4204feb38bd9206"
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

    return response.json().get("score")


def nothing(auth_key):  # score = 596.4027149321267, failed_requests_count = 1687
    """배차 안함"""
    while status == "ready":
        commands = ""
        status = simulate(auth_key, commands)

    return score(auth_key)


def near(auth_key):  # score = 566.7269050312433,  failed_requests_count = 1679
    """주위 정류장의 자전거 개수를 파악하여 배차"""
    status = "ready"
    while status == "ready":
        locations = location_data(auth_key)
        truck = truck_data(auth_key)
        commands = ""
        for i in range(10):
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
                        now + 1 < 3600
                        and locations[now + 1].get("located_bikes_count") < min_num
                    ):  # 위
                        min_num = locations[now + 1].get("located_bikes_count")
                        next_spot = 1
                        dn = 1
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
                    if (
                        now + 5 < 3600
                        and locations[now + 5].get("located_bikes_count") < min_num
                    ):  # 오른쪽
                        min_num = locations[now + 5].get("located_bikes_count")
                        next_spot = 2
                        dn = 5

                    now += dn
                    if idx == 9:
                        command += f"{next_spot}]"
                    else:
                        command += f"{next_spot}, "
                    idx += 1
                    flag = False
                else:
                    while idx < 10 and now_bikes_nums < 3 and loaded_nums:
                        command += "6, "
                        loaded_nums -= 1
                        now_bikes_nums += 1
                        idx += 1
                    while idx < 10 and now_bikes_nums > 3:
                        command += "5, "
                        loaded_nums += 1
                        now_bikes_nums -= 1
                        idx += 1
                    locations[now]["located_bikes_count"] = now_bikes_nums
                    flag = True

            commands += f' {{ "truck_id": {i}, "command": {command}}} '
            if i < 9:
                commands += ","

        status = simulate(auth_key, commands)

    return score(auth_key)


def route_setting(auth_key):  # score = 588.4932070135746, failed_requests_count = 1519
    status = "ready"
    routes = []
    start = [0, 13, 25, 37, 48, 1800, 1813, 1825, 1837, 1848]  # 구역의 크기는 12 x 30

    # 시작 위치로 트럭 이동
    base_command = [[]]  # 시작 위치까지 보낼 명령을 담을 배열
    for i in range(1, 10):
        tmps = []
        tmp = "["
        idx = 0

        if i < 5:  # 절반으로 나눌 때 왼쪽 지역
            while idx < start[i]:  # 위로 이동
                tmp += "1, "
                idx += 1

                if idx % 10 == 0 or idx == start[i]:
                    tmp = tmp[:-2] + "]"
                    comm = f'{{ "truck_id": {i}, "command": {tmp}}}'
                    tmps.append(comm)
                    tmp = "["
        else:  # 절반으로 나눌 때 오른쪽 지역
            while idx < start[i] - 1800:  # 위로 이동
                tmp += "1, "
                idx += 1

                if idx % 10 == 0 or idx == start[i] - 1800:
                    tmp = tmp[:-2] + "]"
                    comm = f'{{ "truck_id": {i}, "command": {tmp}}}'
                    tmps.append(comm)
                    tmp = "["
            idx = 0
            while idx < 30:  # 오른쪽으로 이동
                tmp += "2, "
                idx += 1

                if idx % 10 == 0 or idx == 30:
                    tmp = tmp[:-2] + "]"
                    comm = f'{{ "truck_id": {i}, "command": {tmp}}}'
                    tmps.append(comm)
                    tmp = "["

        base_command.append(tmps)

    # 시작 위치로 트럭 보내기
    for j in range(len(base_command[9])):
        commands = ""
        for i in range(10):
            if len(base_command[i]) > j:
                commands += base_command[i][j] + ", "
        simulate(auth_key, commands[:-2])

    # 트럭들의 경로 만들기
    for i in range(10):
        flag = False
        route = []
        tmp_start = start[i]

        while True:
            if not flag:  # 경로 따라서 올라갈 때
                if route:
                    tmp_start = route[-1] + 60
                for j in range(tmp_start, tmp_start + 1800 - 60, 60):
                    route.append(j)
                    tmp = j
                route.append(tmp + 1)

                tmp_start = route[-1] - 60
                for j in range(tmp_start, tmp_start - 1800 + 60, -60):
                    route.append(j)
                    tmp = j

                if route[-1] == start[i] + 11:
                    flag = True
                    route.append(tmp - 1)
                    continue
                route.append(tmp + 1)
            else:  # 경로 따라서 내려올 때
                tmp_start = route[-1] + 60
                for j in range(tmp_start, tmp_start + 1800 - 60, 60):
                    route.append(j)
                    tmp = j
                route.append(tmp - 1)

                tmp_start = route[-1] - 60
                for j in range(tmp_start, tmp_start - 1800 + 60, -60):
                    route.append(j)
                    tmp = j

                if route[-1] == start[i] + 1:
                    break
                route.append(tmp - 1)
        routes.append(route)

    # 배차 진행
    while status == "ready":
        locations = location_data(auth_key)
        truck = truck_data(auth_key)
        commands = ""

        for i in range(10):
            command = "["
            now = truck[i].get("location_id")  # 현재 트럭 위치
            idx = 0

            while idx < 10:
                tmp = routes[i].index(now)
                if tmp < len(routes[i]) - 1:
                    diff = routes[i][tmp + 1] - routes[i][tmp]
                else:
                    diff = routes[i][0] - routes[i][tmp]
                now += diff

                if diff == 1:
                    command += "1, "
                elif diff == 60:
                    command += "2, "
                elif diff == -1:
                    command += "3, "
                elif diff == -60:
                    command += "4, "
                else:
                    print(f"{i}, {diff}, error")
                    print(routes[i][tmp + 1], routes[i][tmp])
                    print(command)
                    return
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
            if i < 9:
                commands += ","

        status = simulate(auth_key, commands)

    return score(auth_key)


auth_key = start()
print(route_setting(auth_key))
