"""1167 트리의 지름"""
# 처음에 floyd로 했으나 메모리 초과로 실패
import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    """bfs start에서 가장 먼 정점과 그 거리를 구하는 함수

    Args:
        start (int): 시작하는 정점

    Returns:
        radius (list): [가장 먼 정점과의 거리, 가장 먼 정점]
    """
    visit = [-1] * (vertex_num + 1)  # 방문했는 지 확인 겸 떨어진 거리를 저장할 리스트
    queue = deque()
    queue.append(start)
    visit[start] = 0  # 시작 지점까지 거리는 0
    radius = [0, 0]  # 가장 먼 노드와 거리, 가장 먼 노드

    while queue:
        now = queue.popleft()
        for end, dist in tree[now]:
            if visit[end] == -1:  # 아직 탐색하지 않았다면
                visit[end] = visit[now] + dist  # end까지 도달하는 거리를 저장
                queue.append(end)

                # radius 최신화
                if visit[end] > radius[0]:
                    radius = [visit[end], end]
    return radius


vertex_num = int(input())
tree = [[] for _ in range(vertex_num + 1)]
for _ in range(vertex_num):
    v_list = list(map(int, input().split()))
    vertex = v_list[0]
    for i in range(1, len(v_list) - 1, 2):
        tree[vertex].append([v_list[i], v_list[i + 1]])


# 이곳의 그림 참고 / 링크: https://www.acmicpc.net/problem/1967, 문제는 28-3문제
# 아무 정점에서 가장 먼 정점은 지름의 한 점이다
radius = bfs(1)

# 지름의 한 점과 가장 먼 정점과의 거리가 지름이 된다
radius = bfs(radius[1])
print(radius[0])
