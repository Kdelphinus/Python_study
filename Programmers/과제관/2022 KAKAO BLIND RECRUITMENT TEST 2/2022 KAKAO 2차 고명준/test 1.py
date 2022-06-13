"""점수
< 정확성 1, 정확성 2, 효율성, 총점 >
01: 50.444	 53.113	 99.895	 204.19
02: 52.667   53.2968 99.8184 207.0109 / DIFF = 500, WINING_POINT = 5, LOSING_POINT = 3
03: 34.8889  58.3    99.8661 191.7195 / DIFF = 100, WINING_POINT = 5, LOSING_POINT = 5
04: 52.6667  53.2968 99.8184 207.0109 / DIFF = 100, WINING_POINT = 5, LOSING_POINT = 3
05: 52.6667  53.2968 99.8184 207.0109 / DIFF = 100, WINING_POINT = 5, LOSING_POINT = 3, FIRST_TAKEN = 7(2배), SECOND_TAKEN = 15(1.5배)
06: 52.8889  59.9864 99.8126 215.3004 / DIFF = 100, WINING_POINT = 5, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
07: 58.8889  61.6079 99.8374 224.4661 / DIFF = 100, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
08: 54.6667  51.0827 99.8426 206.7762 / DIFF = 100, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배), 질 땐 가중치 없음
09: 52.8889  59.9864 99.8126 215.3004 / DIFF = 100, WINING_POINT = 10, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
10: 48.0     61.1419 99.8103 210.8185 / DIFF = 100, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 10(3배), SECOND_TAKEN = 20(2배)
11: 52.0     60.2472 99.8394 214.5681 / DIFF = 50, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
12: 52.0     60.2472 99.8394 214.5681 / DIFF = 300, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
13: 32.0     52.7878 99.8958 181.662  / DIFF = 100, WINING_POINT = 8, LOSING_POINT = 4, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
14: 52.0     60.2472 99.8394 214.5681 / DIFF = 500, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
15: 32.0     52.7878 99.8958 181.662  / DIFF = 100, WINING_POINT = 10, LOSING_POINT = 5, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
16: 64.8889  54.2716 99.866  222.9099 / DIFF = 25, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
17: 45.5556  55.4864 98.9704 200.4267 / DIFF = 20, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
18: 64.8889  54.2716 99.8966 222.9099 / DIFF = 25, WINING_POINT = 5, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
19: 54.2222  56.5165 94.8413 208.7594 / DIFF = 21, WINING_POINT = 5, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
20: 52.0     60.2472 99.8394 214.5681 / DIFF = 100, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배), 매칭 조건 중 시간 초과에 따른 매칭 조건 제거
21: 52.0     60.2472 99.8394 214.5681 / DIFF = 100, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)

best case
07: 58.8889  61.6079 99.8374 224.4661 / DIFF = 100, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 7(3배), SECOND_TAKEN = 15(2배)
"""

import requests

TOKEN = "c6509aa88ff6cd10ed047d33372178bb"
BASE_URL = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

# 상수 값
DIFF = 100  # 매칭 가능한 등급 차이의 최댓값
WINING_POINT = 7  # 이겼을 때 올라가는 등급
LOSING_POINT = 3  # 졌을 때 내려가는 등급
FIRST_TAKEN = 7  # 아주 크게 이긴 경기의 최장 시간
SECOND_TAKEN = 15  # 크게 이긴 경기의 최장 시간


def start():
    headers = {
        "X-Auth-Token": TOKEN,
        "Content-Type": "application/json",
    }

    data = '{ "problem": 1 }'

    response = requests.post(BASE_URL + "/start", headers=headers, data=data)

    return response.json()["auth_key"]


def WaitingLine(auth_key):
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json",
    }

    response = requests.get(BASE_URL + "/waiting_line", headers=headers)

    return response.json()["waiting_line"]


def GameResult(auth_key):
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json",
    }

    response = requests.get(BASE_URL + "/game_result", headers=headers)

    return response.json()["game_result"]


def UserInfo(auth_key):
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json",
    }

    response = requests.get(BASE_URL + "/user_info", headers=headers)

    return response.json()["user_info"]


def Match(auth_key, pairs):
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json",
    }

    data = f'{{ "pairs": {pairs} }}'

    response = requests.put(BASE_URL + "/match", headers=headers, data=data)

    print(response.json())
    return response.json()["status"]


def ChangeGrade(auth_key, commands):
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json",
    }

    data = f'{{ "commands": [ {commands} ] }}'

    response = requests.put(BASE_URL + "/change_grade", headers=headers, data=data)

    return response.json()["status"]


def Score(auth_key):
    headers = {
        "Authorization": auth_key,
        "Content-Type": "application/json",
    }

    response = requests.get(BASE_URL + "/score", headers=headers)

    return response.json()


# 시작 시, 기다리는 사람 없음 / 모든 유저의 등급은 0으로 시작
auth_key = start()
status = "ready"
turn = 1

# 유저 등급을 가능한 범위의 중간으로 초기화
user = UserInfo(auth_key)
base = ""
for u in user:
    u_id = u["id"]
    base += f'{{ "id": {u_id}, "grade": 5000 }}, '
ChangeGrade(auth_key, base[:-2])


while status == "ready":
    waitting = WaitingLine(auth_key)
    user = UserInfo(auth_key)
    pairs = []
    commands = ""

    # 대기자가 없을 때
    if not waitting:
        status = Match(auth_key, pairs)
        continue

    # 대기하는 유저들을 등급으로 오름차순
    players = []
    for w in waitting:
        id = w["id"]
        grade = user[id - 1]["grade"]
        time = w["from"] - turn
        players.append([id, grade, time])
    players.sort(key=lambda x: x[1])

    # 유저 매칭
    idx = 0
    while idx < len(players):
        pair = []
        while len(pair) < 2 and idx < len(players):
            # 유저 등급의 차이가 많이 나면서 아직 대기할 수 있는 상황일 때
            if (
                idx < len(players) - 1
                and players[idx][1] + DIFF < players[idx + 1][1]
                and players[idx][2] < 14
            ):
                idx += 1
                continue
            pair.append(players[idx][0])
            idx += 1
        if len(pair) == 2:
            pairs.append(pair)

    status = Match(auth_key, pairs)
    turn += 1

    if status == "finished":
        break

    # 결과에 따라 유저 등급 조정
    result = GameResult(auth_key)
    for r in result:
        win_id = r["win"]
        win_id_grade = user[win_id - 1]["grade"]
        lose_id = r["lose"]
        lose_id_grade = user[lose_id - 1]["grade"]
        taken = r["taken"]

        if win_id_grade < 9995:
            if taken <= FIRST_TAKEN:  # 아주 크게 이겼을 때
                win_id_grade += WINING_POINT * 3
            elif taken <= SECOND_TAKEN:  # 크게 이겼을 때
                win_id_grade += WINING_POINT * 2
            else:
                win_id_grade += WINING_POINT
            commands += f'{{ "id": {win_id}, "grade": {win_id_grade} }}, '
        else:
            commands += f'{{ "id": {win_id}, "grade": 9999 }}, '

        if user[lose_id - 1]["grade"] > 2:
            if taken <= FIRST_TAKEN:  # 아주 크게 졌을 때
                lose_id_grade -= LOSING_POINT * 3
            elif taken <= SECOND_TAKEN:  # 크게 졌을 때
                lose_id_grade -= LOSING_POINT * 2
            else:
                lose_id_grade -= LOSING_POINT
            lose_id_grade -= LOSING_POINT
            commands += f'{{ "id": {lose_id}, "grade": {lose_id_grade} }}, '
        else:
            commands += f'{{ "id": {lose_id}, "grade": 0 }}, '
    ChangeGrade(auth_key, commands[:-2])

print(Score(auth_key))
