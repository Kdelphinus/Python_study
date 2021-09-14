"""2019 KAKAO BLIND RECRUITMENT"""


def solution(N, stages):
    answer = []
    fail = [[0, 0] for _ in range(N)]
    user = len(stages)

    for i in range(1, N + 1):
        if user == 0:
            fail[i - 1][0] = 0
            fail[i - 1][1] = i
        else:
            tmp = stages.count(i)
            fail[i - 1][0] = tmp / user
            fail[i - 1][1] = i
            user -= tmp

    fail = sorted(fail, key=lambda x: (-x[0], x[1]))
    for i in range(N):
        answer.append(fail[i][1])

    return answer


# ----------------------------------------------------------------------------------
# 딕셔너리 활용
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N + 1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0

    # result를 그냥 넘기면 자동으로 keys가 들어감
    # 그 뒤, value로 정렬하고 거꾸로 만들어 내림차순을 적용
    return sorted(result, key=lambda x: result[x], reverse=True)
