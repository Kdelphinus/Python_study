"""9935 문자열 폭발"""
import sys

INPUT = sys.stdin.readline


def eod(string: str, boom: str) -> str:
    stack = []
    len_str, len_boom = len(string), len(boom)
    for s in string:
        if (
            len(stack) >= len_boom - 1
            and boom == "".join(stack[len(stack) - len_boom + 1 :]) + s
        ):
            for _ in range(len_boom - 1):
                stack.pop()
            continue
        stack.append(s)

    stack2 = []
    for s in stack:
        if (
            len(stack2) >= len_boom - 1
            and boom == "".join(stack2[len(stack2) - len_boom + 1 :]) + s
        ):
            for _ in range(len_boom - 1):
                stack2.pop()
            continue
        stack2.append(s)

    return "".join(stack2) if stack2 else "FRULA"


if __name__ == "__main__":
    STRING = INPUT().rstrip()
    BOOM = INPUT().rstrip()
    print(eod(STRING, BOOM))

####################################################################################

# 한 번만 돌면서 해결하는 jms7446의 풀이


# def solve(in_str, ptn):
#     stack = []
#     ptn = list(ptn)
#     ptn_len = len(ptn)
#     last_char = ptn[-1]
#     for c in in_str:
#         stack.append(c)
#         if c == last_char and stack[-ptn_len:] == ptn:
#             del stack[-ptn_len:]
#
#     return "".join(x[0] for x in stack) if stack else "FRULA"
#
#
# def main():
#     stdin = sys.stdin
#     S = stdin.readline().strip()
#     P = stdin.readline().strip()
#     print(solve(S, P))
#
#
# if __name__ == "__main__":
#     main()
