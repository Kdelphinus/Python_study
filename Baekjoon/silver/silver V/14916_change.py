def change(n: int) -> int:
    for i in range(n // 5, -1, -1):
        tmp = n - i * 5
        if tmp % 2 == 0:
            return i + tmp // 2
    return -1


if __name__ == "__main__":
    print(change(int(input())))
