"""2021 KAKAO BLIND RECRUITMENT"""


# ----------------------------------------------------------------------------------------------
"""정확성은 통과하지만 효율성을 통과하지 못함"""


def solution(info, query):
    answer = []
    info = [list(i.split()) for i in info]
    for q in query:
        cnt = 0
        q = list(q.split())
        for i in info:
            if q[0] != "-" and q[0] != i[0]:
                continue
            if q[2] != "-" and q[2] != i[1]:
                continue
            if q[4] != "-" and q[4] != i[2]:
                continue
            if q[6] != "-" and q[6] != i[3]:
                continue
            if int(q[7]) <= int(i[4]):
                cnt += 1
        answer.append(cnt)

    return answer
