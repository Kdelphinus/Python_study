"""1707 이분 그래프"""
"""
이분 그래프의 정의: https://gmlwjd9405.github.io/2018/08/23/algorithm-bipartite-graph.html
모범 답안: https://pacific-ocean.tistory.com/349
"""

import sys
from collections import deque

input = sys.stdin.readline


def BFS(start):
    """BFS

    Args:
        start (int): 탐색을 시작할 노드

    Returns:
        (bool): 이분 그래프가 맞는지 안 맞는지 확인하여 리턴
    """
    nodes[start] = 1  # 색깔을 칠해준다
    queue = deque()
    queue.append(start)  # 덱에 시작 노드를 추가
    while queue:
        a = queue.popleft()  # 가장 앞의 노드를 빼고
        for i in lines[a]:  # 그 노드와 연결된 모든 노드를 차례대로 확인
            if nodes[i] == 0:  # 연결된 노드가 아직 색이 없다면
                nodes[i] = -nodes[a]  # 현재 노드와 다른 색을 칠하고
                queue.append(i)  # 덱에 추가
            else:  # 연결된 노드가 색이 있고
                if nodes[i] == nodes[a]:  # 그것이 현재 노드와 색이 갔다면
                    return False
    return True


test = int(input())
for t in range(test):
    isTrue = True  # 이분 그래프인지 판별
    node_num, line_num = map(int, input().split())  # 노드의 개수와 간선 개수
    lines = [[] for _ in range(node_num + 1)]  # 간선의 정보를 저장할 리스트
    nodes = [0 for _ in range(node_num + 1)]  # 각 노드의 색깔을 저장할 리스트
    for _ in range(line_num):  # 이어진 두 점에 각각 이어져있다고 정보를 저장
        a, b = map(int, input().split())
        lines[a].append(b)
        lines[b].append(a)
    for k in range(1, node_num + 1):
        if nodes[k] == 0:  # 아직 색깔이 없다면 그 노드와 연결된 노드들의 색을 칠한다
            if not BFS(k):  # 만약 인접한 노드의 색이 겹친다면
                isTrue = False  # 이분 그래프가 아니다
                break
    print("YES" if isTrue else "NO")
