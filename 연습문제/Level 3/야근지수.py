"""연습문제"""
import heapq  # 효울성때문에 정렬대신 힙을 사용


def solution(n, works):
    if sum(works) <= n:
        return 0

    answer = 0
    heap = []
    for work in works:
        heapq.heappush(heap, [-work, work])

    while n > 0:
        minus, plus = heapq.heappop(heap)
        heapq.heappush(heap, [minus + 1, plus - 1])
        n -= 1

    for minus, plus in heap:
        answer += plus ** 2
    return answer
