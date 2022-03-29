"""2020 카카오 인턴십"""
# 해답: https://dev-note-97.tistory.com/70
# 투 포인터를 사용

from collections import defaultdict


def solution(gems):
    answer = []
    shortest = len(gems) + 1  # 가장 짧은 경우

    start, end = 0, 0
    check = len(set(gems))  # 보석 종류의 수
    contained = defaultdict(int)  # 현재 포함된 보석들의 개수

    while end < len(gems):
        contained[gems[end]] += 1  # 현재 보석 추가
        end += 1

        if len(contained) == check:  # 모든 보석이 들어갔을 때
            while start < end:
                if contained[gems[start]] > 1:  # 보석이 두 개 이상이면 하나 빼도 괜찮다
                    contained[gems[start]] -= 1
                    start += 1
                elif shortest > end - start:  # 뺄 수 없고 최소 거리면 갱신
                    shortest = end - start
                    answer = [start + 1, end]
                    break
                else:  # 뺄 수도 없고 최소 거리도 아니면 그냥 끝냄
                    break
    return answer
