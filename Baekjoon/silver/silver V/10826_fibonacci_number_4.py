def fibo(n: int) -> int:
    if n < 0:
        return -1
    elif n < 2:
        return n

    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == "__main__":
    print(fibo(int(input())))
