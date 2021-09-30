"""나의 풀이"""
from collections import defaultdict


def solution(genres, plays):
    answer = []
    total = []
    kinds = defaultdict(int)

    # 장르별 재생 횟수 저장
    for g, p in zip(genres, plays):
        kinds[g] += p

    # 장르별 재생 횟수, 곡의 재생 횟수, 고유번호를 저장
    for idx, p in enumerate(plays):
        total.append([kinds[genres[idx]], p, idx])

    # 1기준: 장르별 재생 횟수, 2기준: 곡의 재생 횟수로 내림차순
    total.sort(key=lambda x: (-x[0], -x[1]))

    # 베스트앨범 만들기
    tmp = 0  # 장르 확인용 변수
    flag = 0  # 같은 장르가 두 곡까지만 들어가도록 하는 변수
    for g, p, idx in total:
        if tmp != g:  # 다른 장르일 때
            tmp = g
            answer.append(idx)
            flag = 0
        else:  # 같은 장르일 때
            if flag < 1:  # 2곡이 아직 안들어갔다면
                answer.append(idx)
                flag += 1

    return answer


# -----------------------------------------------------------------------------------------------------------------------------------

"""비슷한듯 다른 풀이"""


def solution(genres, plays):
    answer = []
    d = {e: [] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])
    genreSort = sorted(
        list(d.keys()), key=lambda x: sum(map(lambda y: y[0], d[x])), reverse=True
    )
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g], key=lambda x: (x[0], -x[1]), reverse=True)]
        answer += temp[: min(len(temp), 2)]
    return answer
