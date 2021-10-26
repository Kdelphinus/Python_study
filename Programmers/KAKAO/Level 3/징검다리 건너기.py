"""2019 카카오 개발자 겨울 인턴십"""

"""이분 탐색을 사용"""
import sys

sys.setrecursionlimit(10 ** 8)

answer = 0


def solution(stones, k):
    def binary_search(min_v, max_v):
        global answer

        if min_v > max_v:  # 종결 조건
            return

        mid = (min_v + max_v) // 2

        tmp = 0
        for stone in stones:
            if stone < mid:
                tmp += 1
                if tmp == k:  # 건너지 못하는 돌이 연속으로 k번 나오면 못 건넌다
                    break
            else:
                tmp = 0

        if tmp == k:  # mid명까지 징검다리를 못 건널 때
            binary_search(min_v, mid - 1)
        else:  # mid명까지 징검다리를 건널 수 있을 때
            answer = mid
            binary_search(mid + 1, max_v)

    binary_search(1, max(stones))  # 1 ~ max(stones) 명까지 건널 수 있다는 가정 하에 이분 탐색

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

# -------------------------------------------------------------------------

"""정확성 통과, 효율성 실패"""


# def solution(stones, k):
#    answer = float("inf")

#    for idx in range(len(stones) - k + 1):
#        answer = min(max(stones[idx : idx + k]), answer)

#    return answer
