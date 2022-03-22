"""2022 KAKAO BLIND RECRUITMENT"""

from copy import deepcopy

tmp_answer = []
answer = []
apeach = 0
ryan = 0
score_diff = 0


def solution(n, info):
    def DFS(cnt, order):
        global ryan, apeach, score_diff, answer

        if order == 11:
            if cnt > 0:
                tmp_answer[-1] = cnt

            if score_diff < ryan - apeach:
                score_diff = ryan - apeach
                answer = deepcopy(tmp_answer)
            elif score_diff == ryan - apeach and len(answer) > 0:
                for i in range(10, -1, -1):
                    if tmp_answer[i] < answer[i]:
                        break
                    elif tmp_answer[i] > answer[i]:
                        answer = deepcopy(tmp_answer)
                        break
            return

        if info[order] < cnt:
            tmp_answer.append(info[order] + 1)
            ryan += 10 - order
            DFS(cnt - info[order] - 1, order + 1)
            tmp_answer.pop()
            ryan -= 10 - order
        tmp_answer.append(0)
        if info[order] > 0:
            apeach += 10 - order
        DFS(cnt, order + 1)
        tmp_answer.pop()
        if info[order] > 0:
            apeach -= 10 - order

    DFS(n, 0)

    return [-1] if len(answer) == 0 else answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))

tmp_answer = []
answer = []
apeach = 0
ryan = 0
score_diff = 0

print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

tmp_answer = []
answer = []
apeach = 0
ryan = 0
score_diff = 0

print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))

tmp_answer = []
answer = []
apeach = 0
ryan = 0
score_diff = 0

print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
