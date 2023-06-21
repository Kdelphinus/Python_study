"""2019 KAKAO BLIND RECRUITMENT"""


def solution(record):
    answer = []
    logs = []
    nickname = {}
    for i in record:
        tmp = list(i.split())
        logs.append(tmp)

    for log in logs:
        if log[0] == "Enter":
            user, name = log[1], log[2]
            nickname[log[1]] = log[2]
        elif log[0] == "Change":
            user, name = log[1], log[2]
            nickname[log[1]] = log[2]

    for log in logs:
        if log[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(nickname[log[1]]))
        elif log[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(nickname[log[1]]))

    return answer


print(
    solution(
        [
            "Enter uid1234 Muzi",
            "Enter uid4567 Prodo",
            "Leave uid1234",
            "Enter uid1234 Prodo",
            "Change uid4567 Ryan",
        ]
    )
)


# -----------------------------------------------------------------------------------------------
# 최다 추천 풀이
# 메모리 절약, 더욱 간단한 풀이
def solution(record):
    answer = []
    namespace = {}
    printer = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    for r in record:
        rr = r.split(" ")
        if rr[0] in ["Enter", "Change"]:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(" ")[0] != "Change":
            answer.append(namespace[r.split(" ")[1]] + printer[r.split(" ")[0]])

    return answer
