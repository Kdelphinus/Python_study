def fizz_buzz(f: int, b: int, n: int) -> None:
    for i in range(1, n + 1):
        if i % f == 0 and i % b == 0:
            print("FizzBuzz")
        elif i % f == 0:
            print("Fizz")
        elif i % b == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    X, Y, N = map(int, input().split())
    fizz_buzz(X, Y, N)
