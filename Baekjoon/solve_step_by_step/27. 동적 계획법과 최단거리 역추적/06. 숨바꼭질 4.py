"""13913 숨바꼭질 4"""
from collections import deque

# 링크: https://hazung.tistory.com/134


def __path(x):
    """__path x까지 가는데 걸리는 시간과 루트를 출력하는 함수

    Args:
        x (int): 도착한 지점
    """
    arr = []
    temp = x
    # 지나온 노드들을 되돌아가며 루트 저장(그렇기에 루트가 반대로 저장됨)
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(dist[x])  # 걸린 시간
    print(*arr[::-1])  # 목표까지 가는 루트


def bfs(start, goal):
    """bfs start에서 goal까지 가는데 걸리는 시간과 루트를 구하는 함수

    Args:
        start (int): 출발 지점
        goal (int): 목표 지점
    """
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        if x == goal:
            __path(x)
            return
        for i in (x + 1, x - 1, 2 * x):
            if 0 <= i <= 100000 and dist[i] == 0:  # 범위 내에 있고 아직 방문하지 않은 곳일 때
                q.append(i)  # 탐색할 대상으로 추가
                dist[i] = dist[x] + 1  # i까지 가는데 걸리는 시간
                move[i] = x  # i에 오기 전 위치를 저장


start, goal = map(int, input().split())
dist = [0] * 100001  # index까지 가는데 걸리는 시간
move = [0] * 100001  # 직전 위치를 저장
bfs(start, goal)

# ------------------------------------------------------------------------------------

"""이동 과정을 각각 저장했으나 메모리 초과"""

"""
def BFS(start, goal):
    if start == goal:
        return

    queue = deque()
    queue.append(start)
    dp[start] = [start]

    while queue:
        size = len(queue)

        for _ in range(size):
            current = queue.popleft()
            if current + 1 <= 100000 and len(dp[current + 1]) == 0:
                dp[current + 1] = dp[current] + [current + 1]
                queue.append(current + 1)
            if 0 <= current - 1 and len(dp[current - 1]) == 0:
                dp[current - 1] = dp[current] + [current - 1]
                queue.append(current - 1)
            if current * 2 <= 100000 and len(dp[current * 2]) == 0:
                dp[current * 2] = dp[current] + [current * 2]
                queue.append(current * 2)
        dp[current].clear()

        if goal in queue:
            return


start, goal = map(int, input().split())
dp = [[] for _ in range(100001)]
BFS(start, goal)
print(len(dp[goal]) - 1)
print(*dp[goal])
"""
