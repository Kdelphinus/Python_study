"""점수
< 정확성 1,  정확성 2, 효율성,  총점 >
01: 7.915	 57.287	 99.874	 158.14
02: 7.4141   60.0163 98.19   159.4685 / DIFF = 500, WINING_POINT = 5, LOSING_POINT = 3
03: 7.7583   58.6287 98.6818 151.4098 / DIFF = 100, WINING_POINT = 5, LOSING_POINT = 3, ABUSER_POINT = 100
04: 10.2193  57.9741 90.4793 154.2155 / DIFF = 100, WINING_POINT = 7, LOSING_POINT = 3, ABUSER_POINT = 40, FIRST_TAKEN = 7, SECOND_TAKEN = 15, ABUSER_GUIDE = 3
05: 11.2086  57.5511 90.195  154.6678 / DIFF = 100, WINING_POINT = 7, LOSING_POINT = 3, ABUSER_POINT = 40, FIRST_TAKEN = 10, SECOND_TAKEN = 20, ABUSER_GUIDE = 2

이제 abuser 명단에서 빼지 않음
06: 10.5158  57.62   92.4712 155.7399 / DIFF = 150, WINING_POINT = 7, LOSING_POINT = 3, ABUSER_POINT = 40, FIRST_TAKEN = 7, SECOND_TAKEN = 15, ABUSER_GUIDE = 3
07: 10.2193  57.9741 90.4793 154.2155 / DIFF = 100, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 7, SECOND_TAKEN = 15, ABUSER_GUIDE = 3
08: 8.8849   59.7245 98.2768 160.9527 / DIFF = 500, WINING_POINT = 5, LOSING_POINT = 3, FIRST_TAKEN = 7, SECOND_TAKEN = 15, ABUSER_GUIDE = 3

test 1코드로 실행한 test 2
09: 11.296   59.89   84.4849 153.0112 / DIFF = 25, WINING_POINT = 5, LOSING_POINT = 3, FIRST_TAKEN = 7, SECOND_TAKEN = 15

다시 test 2코드로
10: 9.1751   58.3485 95.4987 157.4273 / DIFF = 300, WINING_POINT = 5, LOSING_POINT = 3, FIRST_TAKEN = 10, SECOND_TAKEN = 15, ABUSER_GUIDE = 2
11: 13.4706  57.9901 96.0672 162.6066 / DIFF = 300, WINING_POINT = 7, LOSING_POINT = 3, FIRST_TAKEN = 7, SECOND_TAKEN = 15, ABUSER_GUIDE = 2
12: 14.8546  58.6238 96.1205 165.0704 / DIFF = 300, WINING_POINT = 5, LOSING_POINT = 3, FIRST_TAKEN = 7, SECOND_TAKEN = 15, ABUSER_GUIDE = 2
13: 10.9198  59.471  99.8276 164.3331 / DIFF = 500, WINING_POINT = 5, LOSING_POINT = 3, FIRST_TAKEN = 7, SECOND_TAKEN = 15, ABUSER_GUIDE = 2

best case
12: 14.8546  58.6238 96.1205 165.0704 / DIFF = 300, WINING_POINT = 5, LOSING_POINT = 3, FIRST_TAKEN = 7, SECOND_TAKEN = 15, ABUSER_GUIDE = 2
"""

import requests
from collections import defaultdict

TOKEN = "c6509aa88ff6cd10ed047d33372178bb"
BASE_URL = "https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod"

# 상수값
DIFF = 500  # 매칭 가능한 등급 차이의 최댓값
WINING_POINT = 5  # 이겼을 때 올라가는 등급
LOSING_POINT = 3  # 졌을 때 내려가는 등급
ABUSER_GUIDE = 2  # 고의 패배자로 확정짓는 패배의 수
FIRST_TAKEN = 7  # 아주 크게 이긴 경기의 최장 시간
SECOND_TAKEN = 15  # 크게 이긴 경기의 최장 시간


def start():
    headers = {
        "X-Auth-Token": TOKEN,
        "Content-Type": "application/json",
    }

    data = '{ "problem": 2 }'

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
abuser = defaultdict(int)
fixed_abuser = []

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

        # 고의 패배 유저 확인
        if lose_id_grade > win_id_grade and taken <= 10 and lose_id not in fixed_abuser:
            abuser[lose_id] += 1
            if abuser[lose_id] > ABUSER_GUIDE:
                fixed_abuser.append(lose_id)

        if lose_id in fixed_abuser and taken <= 10 and lose_id_grade > win_id_grade:
            commands += ""
        elif win_id_grade < 9995:
            if taken <= FIRST_TAKEN:  # 아주 크게 이겼을 때
                win_id_grade += WINING_POINT * 3
            elif taken <= SECOND_TAKEN:  # 크게 이겼을 때
                win_id_grade += WINING_POINT * 2
            else:
                win_id_grade += WINING_POINT
            commands += f'{{ "id": {win_id}, "grade": {win_id_grade} }}, '
        else:
            commands += f'{{ "id": {win_id}, "grade": 9999 }}, '

        if (
            lose_id in fixed_abuser and taken <= 10 and lose_id_grade > win_id_grade
        ):  # 고의 패배 유저이면서 고의 패배를 했을 때
            lose_id_grade += WINING_POINT * 5
            commands += f'{{ "id": {lose_id}, "grade": {lose_id_grade} }}, '
        elif lose_id_grade > 2:
            if taken <= FIRST_TAKEN:  # 아주 크게 졌을 때
                lose_id_grade -= LOSING_POINT * 3
            elif taken <= SECOND_TAKEN:  # 크게 졌을 때
                lose_id_grade -= LOSING_POINT * 2
            else:
                lose_id_grade -= LOSING_POINT
            commands += f'{{ "id": {lose_id}, "grade": {lose_id_grade} }}, '
        else:
            commands += f'{{ "id": {lose_id}, "grade": 0 }}, '
    ChangeGrade(auth_key, commands[:-2])

print(Score(auth_key))
