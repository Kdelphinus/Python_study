"""25501 재귀의 귀재"""


import sys

INPUT = sys.stdin.readline
sys.setrecursionlimit(10**8)


def recursion(s, l, r):
    """주어진 함수"""
    global r_cnt

    r_cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def is_palindrome(s):
    """주어진 함수"""
    return recursion(s, 0, len(s) - 1)


if __name__ == "__main__":
    for _ in range(int(INPUT())):
        r_cnt = 0
        p_cnt = is_palindrome(INPUT().rstrip())
        print(f"{p_cnt} {r_cnt}")
