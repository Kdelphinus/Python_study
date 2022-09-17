def solution(a, b):
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]  # 1월 1일이 금요일
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    while a > 1:
        a -= 1
        if a == 2:
            b += 29
        elif a in thirty:
            b += 30
        else:
            b += 31
    return day[b % 7]
