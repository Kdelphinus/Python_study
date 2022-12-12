ONE_DAY_MINUTE = 24 * 60
MONTH = (-1, 31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
MONTH_CONVERT = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


def is_leap_year(y: int) -> int:
    if y % 400 == 0:
        return 1
    if y % 4 == 0 and y % 100:
        return 1
    return 0


def days(y: int, m: int, d: int) -> int:
    ans = d - 1
    m -= 1
    while m:
        ans += MONTH[m][(is_leap_year(y))] if m == 2 else MONTH[m]
        m -= 1
    return ans


def progress_bar(y: int, m: int, d: int, t: list) -> float:
    cnt = days(int(year), MONTH_CONVERT[month], int(day)) * ONE_DAY_MINUTE
    cnt += t[0] * 60 + t[1]
    total = 366 if is_leap_year(int(year)) else 365
    total *= ONE_DAY_MINUTE
    return cnt / total * 100


if __name__ == "__main__":
    tmp1, tmp2 = input().split(",")
    month, day = tmp1.split()
    year, time = tmp2.split()
    print(
        progress_bar(
            int(year), MONTH_CONVERT[month], int(day), list(map(int, time.split(":")))
        )
    )
