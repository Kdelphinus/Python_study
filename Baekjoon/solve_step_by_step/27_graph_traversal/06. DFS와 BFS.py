"""1260 DFS와 BFS"""
import sys

input = sys.stdin.readline


def DFS(num):
    """DFS

    Args:
        num (int): 탐색할 노드 번호
    """
    print(num, end=" ")
    visit[num] = 1
    for i in range(1, node_num + 1):
        if visit[i] == 0 and linked_node[num][i] == 1:  # 아직 탐색하지 않았고 연결되어 있는 노드라면
            DFS(i)  # 탐색


def BFS(num):
    """BFS

    Args:
        num (int): 탐색할 노드 번호
    """
    queue = [num]
    visit[num] = 0  # DFS에서 visit이 이미 1로 바뀌었기에 이번엔 0을 탐색, 1을 미탐색으로 사용
    while queue:  # 아직 queue가 남아있다면
        num = queue[0]
        print(num, end=" ")
        del queue[0]
        for i in range(1, node_num + 1):
            if visit[i] == 1 and linked_node[num][i] == 1:  # 아직 탐색하지 않았고 연결되어 있는 노드라면
                queue.append(i)  # queue에 추가하고
                visit[i] = 0  # 탐색했다고 표시


node_num, line_num, start_node = map(int, input().split())  # 노드의 개수, 간선의 개수, 시작할 노드 번호
linked_node = [[0] * (node_num + 1) for _ in range(node_num + 1)]  # 간선의 정보가 저장될 리스트
visit = [0 for _ in range(node_num + 1)]  # 탐색했는지 확인 용도

for i in range(line_num):
    x, y = map(int, input().split())
    linked_node[x][y] = 1  # x는 y와 연결되어 있음
    linked_node[y][x] = 1  # y는 x와 연결되어 있음

DFS(start_node)
print()
BFS(start_node)
