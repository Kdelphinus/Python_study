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


def isPalindrome(s):
    """주어진 함수"""
    return recursion(s, 0, len(s) - 1)


if __name__ == "__main__":
    for _ in range(int(INPUT())):
        r_cnt = 0
        p_cnt = isPalindrome(INPUT().rstrip())
        print(f"{p_cnt} {r_cnt}")
