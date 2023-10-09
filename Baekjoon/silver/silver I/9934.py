import sys

INPUT = sys.stdin.readline
sys.setrecursionlimit(10**8)


def binary_search(route: list, depth: int) -> None:
    if len(route) == 1:
        BINARY_TREE[depth].extend(route)  # 리스트 안에 원소만 삽입
        return

    mid = len(route) // 2
    BINARY_TREE[depth].append(route[mid])
    binary_search(route[:mid], depth + 1)
    binary_search(route[mid + 1 :], depth + 1)


if __name__ == "__main__":
    K = int(INPUT())
    ROUTE = list(map(int, INPUT().split()))
    BINARY_TREE = [[] for _ in range(K)]
    binary_search(ROUTE, 0)
    for bt in BINARY_TREE:
        print(*bt)
