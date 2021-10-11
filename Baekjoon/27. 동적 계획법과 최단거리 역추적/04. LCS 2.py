"""9252 LCS 2"""


def LCS(string1, string2):
    """LCS LCS를 찾아주는 함수

    Args:
        string1 (str): 주어진 문자열 1
        string2 (str): 주어진 문자열 2

    Returns:
        dp[len1][len2] (list): lcs들이 저장된 배열
    """
    len1 = len(string1)
    len2 = len(string2)

    # dp에선 비어있는 0번 인덱스가 필요하기에 string의 인덱스를 1부터 시작으로 가정
    dp = [[[] for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    for i in range(len1):
        for j in range(len2):
            # 두 문자열이 같을 때
            if string1[i] == string2[j]:
                if dp[i][j]:  # 대각선 위에 저장된 lcs가 있다면
                    for tmp in dp[i][j]:  # 현재 문자열을 이전 lcs에 붙이고 저장
                        dp[i + 1][j + 1].append(tmp + string1[i])
                else:  # 저장된 lcs가 없다면
                    dp[i + 1][j + 1].append(string1[i])  # 현재 문자열만 저장

            # 두 문자열이 다를 때
            else:
                if not dp[i + 1][j] and not dp[i][j + 1]:  # 왼쪽과 위쪽이 전부 비어있다면
                    continue  # 넘어감
                elif not dp[i + 1][j]:  # 위쪽만 비어있다면
                    dp[i + 1][j + 1] = dp[i][j + 1]  # 왼쪽 것을 가져옴
                elif not dp[i][j + 1]:  # 왼쪽만 비어있다면
                    dp[i + 1][j + 1] = dp[i + 1][j]  # 위쪽 것을 가져옴
                else:  # 둘 다 있다면 둘 중 긴 lcs를 가진 것을 가져옴
                    if len(dp[i][j + 1][0]) < len(dp[i + 1][j][0]):
                        dp[i + 1][j + 1] = dp[i + 1][j]
                    else:
                        dp[i + 1][j + 1] = dp[i][j + 1]

    return dp[len1][len2]


string1 = input()
string2 = input()
lcs = LCS(string1, string2)
if lcs:
    print(len(lcs[0]))
    print(lcs[0])  # 아무 lcs나 출력해도 됨
else:
    print(0)
