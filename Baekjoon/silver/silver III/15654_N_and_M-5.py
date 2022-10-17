import enum


def nnm(n: int, m: int, cnt: int):
    if cnt == m:
        print(*tmp)
        return

    for idx, num in enumerate(numbers):
        if not visit[idx]:
            visit[idx] = 1
            tmp.append(num)
            nnm(n, m, cnt + 1)
            visit[idx] = 0
            tmp.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    tmp, visit = [], [0] * n
    numbers = sorted(list(map(int, input().split())))
    nnm(n, m, 0)
