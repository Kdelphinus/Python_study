"""2606 바이러스"""
import sys

input = sys.stdin.readline
cnt = -1  # 1번 컴퓨터는 제외


def DFS(num):
    """DFS

    Args:
        num (int): 탐색할 컴퓨터 번호
        cnt (int): 1번 컴퓨터와 연결된 컴퓨터의 개수
    """
    global cnt

    cnt += 1
    visit[num] = 1
    for i in range(1, node_num + 1):
        if visit[i] == 0 and linked_node[num][i] == 1:
            DFS(i)


node_num = int(input())
visit = [0 for _ in range(node_num + 1)]
linked_node_num = int(input())
linked_node = [[0] * (node_num + 1) for _ in range(node_num + 1)]

for i in range(linked_node_num):
    x, y = map(int, input().split())
    linked_node[x][y] = 1
    linked_node[y][x] = 1

DFS(1)
print(cnt)
