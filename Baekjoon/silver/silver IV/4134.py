def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def next_prime_number(n: int) -> int:
    while True:
        if is_prime(n):
            return n
        n += 1


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        print(next_prime_number(int(input())))
