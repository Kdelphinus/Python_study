pwds = {}


def init_passwd(n: int):
    for _ in range(n):
        id_name, pwd = input().split()
        pwds[id_name] = pwd


def find_passwd(m: int):
    for _ in range(m):
        print(pwds[input()])


if __name__ == "__main__":
    n, m = map(int, input().split())
    init_passwd(n)
    find_passwd(m)
