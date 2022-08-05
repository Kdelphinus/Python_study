"""연습 문제"""


def max_divisor(num: int):
    if num == 1:
        return 0
    for i in range(int(num ** 0.5), 1, -1):
        if num % i == 0 and num // i < 1000000000:
            return num // i
    return 1


def number_block(begin: int, end: int):
    block = []
    for i in range(begin, end + 1):
        block.append(max_divisor(i))
    return block


def main():
    begin, end = map(int, input().split())
    print(number_block(begin, end))


if __name__ == "__main__":
    main()
