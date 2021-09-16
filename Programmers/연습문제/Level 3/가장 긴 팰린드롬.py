"""연습문제"""


def solution(s):
    answer = 1
    dp = [[0] * len(s) for _ in range(len(s))]
    dp[0][0] = 1
    for i in range(1, len(s)):
        dp[i][i] = 1  # 한 글자는 모두 팰린드롬
        if s[i - 1] == s[i]:  # 두 글자 팰린드롬
            dp[i - 1][i] = 2
            answer = 2

    for end in range(2, len(s)):
        for start in range(len(s) - end):
            # 맨 앞과 맨 뒤가 같고 그 사이의 글자들이 팰린드롬이면 팰린드롬이다
            if s[start] == s[start + end] and dp[start + 1][start + end - 1]:
                dp[start][start + end] = dp[start + 1][start + end - 1] + 2
                answer = max(answer, dp[start][start + end])

    return answer


print(solution("abcdcba"))
print(solution("abacde"))
