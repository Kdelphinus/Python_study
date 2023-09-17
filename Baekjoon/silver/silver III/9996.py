def is_pattern(string: str) -> bool:
    check = [False] * len(string)
    for i in range(len(PATTERN[0])):
        if PATTERN[0][i] != string[i] or check[i]:
            return False
        check[i] = True
    for i in range(len(PATTERN[1])):
        if (
            PATTERN[1][len(PATTERN[1]) - i - 1] != string[len(string) - i - 1]
            or check[len(string) - i - 1]
        ):
            return False
        check[len(string) - i - 1] = True
    return True


n = int(input())
PATTERN = list(input().split("*"))
for _ in range(n):
    tmp = input()
    print("DA") if is_pattern(tmp) else print("NE")
