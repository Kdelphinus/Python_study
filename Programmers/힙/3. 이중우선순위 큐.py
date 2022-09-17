"""나의 풀이 / 힙을 쓰지 않음"""
from collections import deque


def solution(operations):
    answer = deque()

    for operation in operations:
        order, number = operation.split()
        answer = sorted(list(answer))
        answer = deque(answer)

        if order == "I":
            answer.append(int(number))
        else:
            if answer and number == "1":
                answer.pop()
            elif answer and number == "-1":
                answer.popleft()

    answer = sorted(list(answer))

    return [answer[-1], answer[0]] if answer else [0, 0]


# -------------------------------------------------------------------------------------------------

"""힙을 활용한 풀이"""
from heapq import heappush, heappop


def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":  # 최댓값을 제거할 때
            if max_heap:
                heappop(max_heap)  # 최댓값을 제거

                # 힙이 비었거나 최댓값보다 최솟값이 커진 경우, 힙을 초기화
                if not max_heap or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap:
                heappop(min_heap)  # 최솟값 제거

                # 힙이 비었거나 최댓값보다 최솟값이 커진 경우, 힙을 초기화
                if not min_heap or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:  # 수를 삽입할 때
            num = int(arg[2:])
            heappush(max_heap, -num)  # 힙의 특성에 따라 음수로 삽입
            heappush(min_heap, num)
    if not min_heap:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]
