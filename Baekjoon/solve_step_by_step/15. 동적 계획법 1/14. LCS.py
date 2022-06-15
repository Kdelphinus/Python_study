"""9251 LCS"""

# 문자열 2개를 받음
string_1 = input()
string_2 = input()
len_1 = len(string_1)
len_2 = len(string_2)

# len_1 x len_2 행렬 생성
dp = [[0] * (len_2 + 1) for _ in range(len_1 + 1)]

for i in range(len_1):
    for j in range(len_2):
        if string_1[i] == string_2[j]:  # 같으면 직전 최장 길이에 1을 추가한다
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:  # 다르면 뒤에 붙이지 못하므로 위의 값(dp[i][j + 1])과 왼쪽 값(dp[i + 1][j]) 중 긴 길이를 가져온다
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

print(dp[len_1][len_2])
