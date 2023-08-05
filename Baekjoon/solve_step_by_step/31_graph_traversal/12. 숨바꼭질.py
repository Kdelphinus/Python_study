"""1697 숨바꼭질"""
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
#
# def BFS(n, k):
#     """BFS
#
#     Args:
#         n (int): 현재 위치
#         k (int): 탐색할 위치
#
#     Returns:
#         time (int): 현재 위치에서 탐색할 위치까지 가는데 걸리는 시간
#     """
#     time = 0  # 움직인 시간
#
#     if n == k:  # 만약 동일한 위치에 있다면 바로 찾는다
#         return time
#
#     log = [0] * 100001  # 0은 탐색 전, 1은 탐색 후
#     queue = deque()  # 큐를 만들고
#     queue.append(n)  # 현재 위치를 넣는다
#
#     while True:
#         size = len(queue)  # 현재 있을 수 있는 위치의 개수
#         time += 1  # 시간을 더하고
#
#         for i in range(size):
#             current = queue.popleft()  # 현재 있을 수 있는 위치 중 하나를 빼서 갈 수 있는 위치들을 넣는다
#             if 0 <= current * 2 <= 100000 and log[current * 2] == 0:  # 아직 지나가지 않은 곳이라면
#                 queue.append(current * 2)  # 순간이동
#                 log[current * 2] = 1  # 탐색 표시
#             if 0 <= current - 1 <= 100000 and log[current - 1] == 0:  # 아직 지나가지 않은 곳이라면
#                 queue.append(current - 1)  # 뒤로 한 칸
#                 log[current - 1] = 1  # 탐색 표시
#             if 0 <= current + 1 <= 100000 and log[current + 1] == 0:  # 아직 지나가지 않은 곳이라면
#                 queue.append(current + 1)  # 앞으로 한 칸
#                 log[current + 1] = 1  # 탐색 표시
#
#         if k in queue:  # 만약 구한 위치 중 찾을 위치와 동일한 위치가 있으면 함수 종료
#             return time
#
#
# n, k = map(int, input().split())  # 찾는 사람 위치, 숨은 사람 위치
# print(BFS(n, k))


################################################################################################################################
"""2022.03.18"""

from collections import deque


def BFS(position, target):
    if position == target:
        return 0

    time = 0
    visit = [0] * 100001
    queue = deque()
    queue.append(position)

    while queue:
        time += 1
        for _ in range(len(queue)):
            now = queue.popleft()
            if now - 1 >= 0 and visit[now - 1] == 0:
                if target == now - 1:
                    return time
                visit[now - 1] = 1
                queue.append(now - 1)
            if now + 1 <= 100000 and visit[now + 1] == 0:
                if target == now + 1:
                    return time
                visit[now + 1] = 1
                queue.append(now + 1)
            if now * 2 <= 100000 and visit[now * 2] == 0:
                if target == now * 2:
                    return time
                visit[now * 2] = 1
                queue.append(now * 2)

    return -1


subin, sister = map(int, input().split())
print(BFS(subin, sister))
