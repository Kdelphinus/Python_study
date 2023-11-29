from collections import deque


def kevin_bacon(me: int, n: int, linked: list):
    queue = deque()
    queue.append((me, 0))
    visited = [0] * n
    visited[me] = 1

    while queue:
        user, dist = queue.popleft()

        for i in range(n):
            if not visited[i] and i in linked[user]:
                queue.append((i, dist + 1))
                visited[i] = dist + 1

    return sum(visited) - 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    linked = [[] for _ in range(n)]
    for _ in range(m):
        u1, u2 = map(int, input().split())
        linked[u1 - 1].append(u2 - 1)
        linked[u2 - 1].append(u1 - 1)

    ans, min_kevin = 0, float("inf")
    for i in range(n):
        tmp = kevin_bacon(i, n, linked)
        if min_kevin > tmp:
            ans, min_kevin = i, tmp
    print(ans + 1)
