def lcs3(str1: str, str2: str, str3: str) -> int:
    dp = [
        [[0 for _ in range(len(str3) + 1)] for __ in range(len(str2) + 1)]
        for ___ in range(len(str1) + 1)
    ]
    for i in range(len(str1)):
        for j in range(len(str2)):
            for k in range(len(str3)):
                dp[i + 1][j + 1][k + 1] = (
                    dp[i][j][k] + 1
                    if str1[i] == str2[j] == str3[k]
                    else max(
                        dp[i][j + 1][k + 1], dp[i + 1][j][k + 1], dp[i + 1][j + 1][k]
                    )
                )
    return dp[len(str1)][len(str2)][len(str3)]


if __name__ == "__main__":
    STR1 = input()
    STR2 = input()
    STR3 = input()
    print(lcs3(STR1, STR2, STR3))
