from string import ascii_uppercase


BASE = {}
for i in range(10):
    BASE[i] = str(i)
for i, a in enumerate(list(ascii_uppercase)):
    BASE[i + 10] = a


def convert_base(n: int, b: int) -> str:
    if n == 0:
        return "0"

    num = ""
    while n:
        num = BASE[n % b] + num
        n //= b

    return num


if __name__ == "__main__":
    N, B = map(int, input().split())
    print(convert_base(N, B))
