import sys

INPUT = sys.stdin.readline


def check_permutation(n: int, lst: list) -> str:
    for i in range(n):
        if i == 0:
            lst[i] = min(lst[i], n - lst[i] + 1)
            continue
        if (lst[i - 1] <= n - lst[i] + 1) and lst[i - 1] > lst[i]:
            lst[i] = n - lst[i] + 1
        elif (lst[i - 1] > n - lst[i] + 1) and lst[i - 1] <= lst[i]:
            lst[i] = lst[i]
        elif (lst[i - 1] <= n - lst[i] + 1) and lst[i - 1] <= lst[i]:
            lst[i] = min(n - lst[i] + 1, lst[i])
        else:
            return "NO"
    return "YES"


if __name__ == "__main__":
    T = int(INPUT())
    for _ in range(T):
        N = int(INPUT())
        print(check_permutation(N, list(map(int, INPUT().split()))))
