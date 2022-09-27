def check_key(n: int, i: int, break_key: list):
    plus, minus = 0, 0
    for j in set(str(n + i)):
        if j in break_key:
            break
    else:
        plus = len(str(n + i)) + i
    if n >= i:
        for j in set(str(n - i)):
            if j in break_key:
                break
        else:
            minus = len(str(n - i)) + i

    if plus and minus:
        return min(plus, minus)
    elif plus:
        return plus
    elif minus:
        return minus
    return 0


def move_to_channel(n: int, break_key: list):
    if "100" == str(n):
        return 0

    if len(break_key) == 10:
        return abs(n - 100)

    i = 0
    while True:
        chekc = check_key(n, i, break_key)
        if chekc:
            return min(abs(n - 100), chekc)
        i += 1


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    break_key = list(input().split()) if m else list()
    print(move_to_channel(n, break_key))
