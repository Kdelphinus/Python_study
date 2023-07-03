# 17103 골드바흐 파티션


BOUNDARY = 1000000
NUMBERS = [True] * (BOUNDARY + 1)


def prime_number_list() -> None:
    NUMBERS[0], NUMBERS[1] = False, False
    for i in range(2, BOUNDARY + 1):
        if NUMBERS[i]:
            for j in range(i + i, BOUNDARY + 1, i):
                if j <= BOUNDARY:
                    NUMBERS[j] = False


def goldbach_partition(n: int) -> int:
    cnt = 0
    for i in range(2, n // 2 + 1):
        if NUMBERS[i] and NUMBERS[n - i]:
            cnt += 1
    return cnt


if __name__ == "__main__":
    T = int(input())
    prime_number_list()
    for _ in range(T):
        print(goldbach_partition(int(input())))
