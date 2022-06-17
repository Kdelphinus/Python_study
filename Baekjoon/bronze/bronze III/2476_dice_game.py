"""너무 복잡하게 생각해서 풀었다"""

from collections import Counter


def main():
    num = int(input())
    price = 0
    for _ in range(num):
        dices = list(map(int, input().split()))
        dices = Counter(dices).most_common()
        dices.sort(key=lambda x: (-x[1], -x[0]))
        if dices[0][1] == 3:
            price = max(price, 10000 + 1000 * dices[0][0])
        elif dices[0][1] == 2:
            price = max(price, 1000 + 100 * dices[0][0])
        elif dices[0][1] == 1:
            price = max(price, dices[0][0] * 100)
    print(price)


if __name__ == "__main__":
    main()
