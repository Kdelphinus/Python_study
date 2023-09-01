import sys

INPUT = sys.stdin.readline


def buy_fruits(money, fruits):
    fullness = 0
    fruits.sort(key=lambda x: (-x[1], -x[0]))
    for cnt, fruit in fruits:
        if money < cnt:
            fullness += fruit * money
            break
        fullness += fruit * cnt
        money -= cnt
    return fullness


if __name__ == "__main__":
    N, K = map(int, input().split())
    FRUITS = []
    for _ in range(N):
        P, C = map(int, input().split())
        FRUITS.append((P, C // P))
    print(buy_fruits(K, FRUITS))
