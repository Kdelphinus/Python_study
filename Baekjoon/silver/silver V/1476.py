MAX_YEAR = 7980


def date_cal(earth: int, sun: int, moon: int) -> int:
    year = 1
    while MAX_YEAR >= year:
        tmp_e = year % 15 if year % 15 else 15
        tmp_s = year % 28 if year % 28 else 28
        tmp_m = year % 19 if year % 19 else 19

        if tmp_e == earth and tmp_s == sun and tmp_m == moon:
            return year
        year += 1


if __name__ == "__main__":
    E, S, M = map(int, input().split())
    print(date_cal(E, S, M))
