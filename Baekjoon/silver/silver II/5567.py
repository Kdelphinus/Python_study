import sys
from collections import deque

INPUT = sys.stdin.readline


def bfs() -> int:
    queue = deque([(1, 0)])
    visited = [0] * (N + 1)
    visited[1] = 1

    while queue:
        friend, distance = queue.popleft()

        for another_friend in FRIENDS[friend]:
            if not visited[another_friend] and distance < 2:
                queue.append((another_friend, distance + 1))
                visited[another_friend] = 1

    return sum(visited) - 1


if __name__ == "__main__":
    N = int(INPUT())
    M = int(INPUT())
    FRIENDS = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, INPUT().split())
        FRIENDS[A].append(B)
        FRIENDS[B].append(A)
    print(bfs())
