"""2019 KAKAO BLIND RECRUITMENT"""

# 해설: https://kyome.tistory.com/109

from itertools import combinations


def solution(relation):
    total = []  # 조합할 수 있는 모든 후보키 후보
    unique_index = []  # 유일성을 지니는 후보키 후보
    row_size = len(relation)
    col_size = len(relation[0])

    # 조합할 수 있는 모든 후보키 후보를 추가
    for i in range(1, col_size + 1):
        total.extend([set(k) for k in combinations(range(col_size), i)])

    for comb in total:
        valid_set = set()  # 후보키로 적합한지 확인하기 위한 셋
        for row in range(row_size):
            temp = ""
            for col in comb:
                temp += relation[row][col]  # 후보키 검증을 위하여 문자열로 저장
            valid_set.add(temp)  # 셋에 추가

        if len(valid_set) == row_size:  # 중복이 없다면 길이가 행만큼 나올 것
            unique_index.append(comb)

    del_set = set()  # 최소성을 만족하지 않는 후보키 후보들
    for standard in unique_index:  # 비교 기준이 될 후보키 후보
        for idx, compare in enumerate(unique_index):  # 비교할 후보키 후보와 그 인덱스
            # standard가 compare의 교집합이고 둘이 동일하지 않으면 compare는 최소성을 만족하지 못함
            if standard.issubset(compare) and standard != compare:
                del_set.add(idx)

    return len(unique_index) - len(del_set)  # 유일성 지키는 후보 - 최소성을 못지키는 후보


print(
    solution(
        [
            ["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"],
        ]
    )
)


# -----------------------------------------------------------------------------------

"""좀 더 간단한 풀이"""
from itertools import combinations


def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    # 모든 후보키 후보들을 구함
    candidates = []
    for i in range(1, n_col + 1):
        candidates.extend(combinations(range(n_col), i))

    # 유일성을 만족하는 후보키 후보만 빼냄
    final = []
    for keys in candidates:
        tmp = [tuple([profile[key] for key in keys]) for profile in relation]
        if len(set(tmp)) == n_row:
            final.append(keys)

    # final에서 최소성도 만족하는 후보키 후보만 남김
    answer = set(final)
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if set(final[i]).issubset(set(final[j])):
                answer.discard(final[j])

    return len(answer)


print(
    solution(
        [
            ["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"],
        ]
    )
)

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
