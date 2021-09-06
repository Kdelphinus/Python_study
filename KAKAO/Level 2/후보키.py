"""2019 KAKAO BLIND RECRUITMENT"""


# -----------------------------------------------------------------------------------

"""첫 풀이, 85%의 정답률"""
from itertools import combinations


def solution(relations):
    answer = 0
    idx = 1
    num = len(relations)
    kinds = len(relations[0])
    check = [i for i in range(kinds)]

    while len(check) >= idx:
        check_idx = list(combinations(check, idx))
        for rel in check_idx:
            tmp = []
            flag = True
            for i in range(num):
                tmp2 = []
                for j in rel:
                    tmp2.append(relations[i][j])
                if tmp2 in tmp:
                    flag = False
                    break
                tmp.append(tmp2)
            if flag:
                answer += 1
                for j in rel:
                    if j in check:
                        del check[check.index(j)]
        idx += 1

    return answer
