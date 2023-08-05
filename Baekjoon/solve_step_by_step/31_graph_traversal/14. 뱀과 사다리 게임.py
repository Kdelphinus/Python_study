"""16928 뱀과 사다리 게임 / gold V"""

import sys
from collections import deque

INPUT = sys.stdin.readline


def bfs(start: list, board: list):
    queue = deque()
    queue.append(start)
    visited = [0] * 101

    while queue:
        curr = queue.popleft()

        for i in range(1, 7):
            next = curr + i
            if next < 101:
                while board[next]:
                    next = board[next]
                if next == 100:
                    return visited[curr] + 1
                if not visited[next]:
                    queue.append(next)
                    visited[next] = visited[curr] + 1
    return -1


def main():
    board = [0] * 101
    n, m = map(int, INPUT().split())
    for _ in range(n + m):
        s, g = map(int, INPUT().split())
        board[s] = g
    cnt = bfs(1, board)
    print(cnt if cnt > 0 else "impossible")


if __name__ == "__main__":
    main()
