import sys

INPUT = sys.stdin.readline


def polar_bear(s: str) -> int:
    idx, day, tmp, stack = 0, 0, 0, []
    while idx < len(s):
        while idx < len(s) and s[idx] == "(":
            if stack and stack[-1] == ")":
                stack.pop()
                tmp += 1
            else:
                stack.append(s[idx])
                day = max(day, tmp)
                tmp = 0
            idx += 1
        while idx < len(s) and s[idx] == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                tmp += 1
            else:
                stack.append(s[idx])
                day = max(day, tmp)
                tmp = 0
            idx += 1
    day = max(day, tmp)
    return -1 if stack else day


if __name__ == "__main__":
    _ = int(INPUT())
    string = INPUT().rstrip()
    print(polar_bear(string))
