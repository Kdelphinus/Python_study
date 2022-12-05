from collections import deque


def changer(start: int, goal: int) -> int:
    if start == goal:
        return 1

    queue = deque()
    queue.append((start, 1))

    while queue:
        num, cnt = queue.popleft()

        if num * 2 == goal or num * 10 + 1 == goal:
            return cnt + 1

        if num * 2 < goal:
            queue.append((num * 2, cnt + 1))
        if num * 10 + 1 < goal:
            queue.append((num * 10 + 1, cnt + 1))

    return -1


if __name__ == "__main__":
    A, B = map(int, input().split())
    print(changer(A, B))
