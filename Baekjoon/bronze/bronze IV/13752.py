def draw_histogram(n: int) -> None:
    print("=" * n)


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        draw_histogram(int(input()))
