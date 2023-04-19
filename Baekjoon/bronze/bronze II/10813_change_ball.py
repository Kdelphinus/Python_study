def change_ball(a: int, b: int) -> None:
    tmp = balls[a]
    balls[a] = balls[b]
    balls[b] = tmp


if __name__ == "__main__":
    N, M = map(int, input().split())
    balls = [i for i in range(N + 1)]
    for _ in range(M):
        N1, N2 = map(int, input().split())
        change_ball(N1, N2)
    print(*balls[1:])
