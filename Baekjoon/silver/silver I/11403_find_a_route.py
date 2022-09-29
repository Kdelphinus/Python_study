from collections import deque


def find_route(start: int, linked: list):
    queue = deque()
    queue.append(start)
    visited = [0] * len(linked)

    while queue:
        now = queue.popleft()

        for next_p, link in enumerate(linked[now]):
            if link and not visited[next_p]:
                visited[next_p] = 1
                queue.append(next_p)
    return visited


if __name__ == "__main__":
    n = int(input())
    linked = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        print(*find_route(i, linked))
