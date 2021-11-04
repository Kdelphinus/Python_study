"""11725 트리의 부모 찾기"""
import sys
from collections import deque

input = sys.stdin.readline


def bfs(num, root):
    """bfs bfs를 통해 부모 노드를 찾는 함수

    Args:
        num (int): 노드의 개수
        root (int): root node

    Returns:
        parent_node (list): 각 인덱스마다 부모 노드를 저장한 리스트
    """
    parent_node = [0] * (num + 1)
    queue = deque()
    queue.append(root)

    while queue:
        now = queue.popleft()
        for next in tree[now]:
            if parent_node[next] == 0:
                parent_node[next] = now
                queue.append(next)

    return parent_node


num = int(input())
tree = [[] for _ in range(num + 1)]
for _ in range(num - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent_node = bfs(num, 1)
for i in parent_node[2:]:
    print(i)

# ---------------------------------------------------------------------------------------

"""dfs를 사용한 풀이"""
node = int(input())
node_graph = [[] for _ in range(node + 1)]
parent = [[] for _ in range(node + 1)]

# 트리를 그래프 형태로 생성
for _ in range(node - 1):
    i, j = map(int, input().split())
    node_graph[i].append(j)
    node_graph[j].append(i)


def dfs(graph_list, start, parent):
    stack = [start]

    while stack:
        node = stack.pop()
        for i in graph_list[node]:
            parent[i].append(node)
            stack.append(i)
            graph_list[i].remove(node)
    return parent


for i in list(dfs(node_graph, 1, parent))[2:]:
    print(i[0])
