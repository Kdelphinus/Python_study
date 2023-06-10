INF = float("inf")


def size() -> int:
    n = int(input())
    min_x, max_x, min_y, max_y = INF, -INF, INF, -INF
    for _ in range(n):
        x, y = map(int, input().split())
        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)
    area = (max_x - min_x) * (max_y - min_y)
    return area if area >= 0 else 0


if __name__ == "__main__":
    print(size())
