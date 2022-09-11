import sys


INPUT = sys.stdin.readline


def main():
    s = set()
    n = int(INPUT())
    for _ in range(n):
        orders = INPUT().split()
        order = orders[0]
        try:
            value = int(orders[1])
        except:
            pass
        if order == "all":
            s = {i for i in range(1, 21)}
        elif order == "empty":
            s.clear()
        elif order == "add":
            s.add(value)
        elif order == "remove":
            s.discard(value)  # discard는 remove와 다르게 값이 없는 경우 연산 무시
        elif order == "check":
            print(1 if value in s else 0)
        elif order == "toggle":
            s.discard(value) if value in s else s.add(value)
        else:
            print("wrong order")


if __name__ == "__main__":
    main()
