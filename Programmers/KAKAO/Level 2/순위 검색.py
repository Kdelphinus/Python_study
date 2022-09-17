"""2021 KAKAO BLIND RECRUITMENT"""
# 링크: https://whwl.tistory.com/193

from collections import defaultdict
from itertools import combinations


def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        info_key = info[:-1]  # 점수를 제외한 나머지 조건
        info_val = int(info[-1])  # 지원자 점수

        # 합격할 수 있는 모든 조건을 key로, 지원자 점수를 value로 설정
        for i in range(5):
            for c in combinations(info_key, i):
                tmp_key = "".join(c)
                info_dict[tmp_key].append(info_val)

    # 조건 안에 들어있는 지원자 점수들을 오름차순으로 정렬
    for key in info_dict.keys():
        info_dict[key].sort()

    for query in queries:
        query = query.split(" ")
        query_score = int(query[-1])  # 최소 점수
        query = query[:-1]  # 합격 조건들

        for i in range(3):  # 'and' 제거
            query.remove("and")
        while "-" in query:  # '-'을 제거
            query.remove("-")
        tmp_q = "".join(query)  # 조건들을 공백없이 합친다

        if tmp_q in info_dict:  # 합격조건에 부합하는 합격자가 있다면
            scores = info_dict[tmp_q]  # 합격자들의 점수를 가져온다
            if len(scores) > 0:  # 지원한 점수가 하나라도 존재할 때
                start, end = 0, len(scores)
                while end > start:  # 이분 탐색으로 최소 점수를 넘은 합격자를 찾는다
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:  # 합격 조건에 부합하는 합격자가 없다면
            answer.append(0)  # 모두 불합격

    return answer


infos = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
]
queries = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150",
]

print(solution(infos, queries))

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
