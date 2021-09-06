"""2019 KAKAO BLIND RECRUITMENT"""

# 해설: https://kyome.tistory.com/109

from itertools import combinations


def solution(relation):
    total = []
    unique_index = []
    row_size = len(relation)
    col_size = len(relation[0])

    for i in range(1, col_size + 1):
        total.extend([set(k) for k in combinations([j for j in range(col_size)], i)])

    for comb in total:
        valid_set = set()
        for row in range(row_size):
            temp = ""
            for col in comb:
                temp += relation[row][col]
            valid_set.add(temp)

        if len(valid_set) == row_size:
            unique_index.append(comb)

    del_set = set()
    for standard in unique_index:
        for idx, compare in enumerate(unique_index):
            if standard.issubset(compare) and standard != compare:
                del_set.add(idx)

    return len(unique_index) - len(del_set)


# -----------------------------------------------------------------------------------

"""첫 풀이, 85%의 정답률"""


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
