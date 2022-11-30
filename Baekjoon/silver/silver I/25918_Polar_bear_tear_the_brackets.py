# joon6924(wonjilee)의 풀이 참고
import sys

INPUT = sys.stdin.readline


def polar_bear(s: str) -> int:
    cnt, day = 0, 0
    for a in s:
        if a == "(":
            cnt += 1
        elif a == ")":
            cnt -= 1
        day = max(day, abs(cnt))
    return -1 if cnt else day


if __name__ == "__main__":
    _ = int(INPUT())
    string = INPUT().rstrip()
    print(polar_bear(string))
