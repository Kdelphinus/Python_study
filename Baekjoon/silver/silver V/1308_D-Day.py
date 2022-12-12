# python의 datetime 모듈로 간단하게 할 수도 있지만 공부를 위해 구현

MONTH = (-1, 31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def is_thousand(t: list, d: list) -> bool:
    if d[0] - t[0] < 1000:
        return False
    if d[0] - t[0] > 1000:
        return True
    if d[1] < t[1]:
        return False
    if d[1] == t[1] and d[2] < t[2]:
        return False
    return True


def is_leap_year(y: int) -> int:
    if y % 400 == 0:
        return 1
    if y % 4 == 0 and y % 100:
        return 1
    return 0


def last_year(t: list) -> int:
    y, m, d = t
    ans = d - 1
    m -= 1
    while m:
        ans += MONTH[m][(is_leap_year(y))] if m == 2 else MONTH[m]
        m -= 1
    return ans


def first_year(t: list) -> int:
    y, m, d = t
    ans = MONTH[m][(is_leap_year(y))] - d if m == 2 else MONTH[m] - d
    ans += 1
    m += 1
    while m < 13:
        ans += MONTH[m][(is_leap_year(y))] if m == 2 else MONTH[m]
        m += 1
    return ans


def print_d_day(t: list, d: list) -> str:
    if is_thousand(t, d):
        return "gg"

    if t[0] < d[0]:
        day = first_year(t) + last_year(d)
        for y in range(t[0] + 1, d[0]):
            day += 366 if is_leap_year(y) else 365
    else:
        day = last_year(d) - last_year(t)

    return f"D-{day}"


if __name__ == "__main__":
    today = list(map(int, input().split()))
    d_day = list(map(int, input().split()))
    print(print_d_day(today, d_day))
