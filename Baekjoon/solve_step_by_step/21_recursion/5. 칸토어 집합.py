"""4779 칸토어 집합"""


# sys.stdin.readline은 EOFError을 raise하지 않음


def cantorian_set(n: int) -> str:
    if n == 0:
        return "-"
    blank = " " * 3 ** (n - 1)
    pattern = cantorian_set(n - 1)
    return pattern + blank + pattern


if __name__ == "__main__":
    while True:
        try:
            print(cantorian_set(int(input())))
        except EOFError:
            break
