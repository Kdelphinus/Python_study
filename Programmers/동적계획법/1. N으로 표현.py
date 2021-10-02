"""나의 풀이, 질문하기에서 참고함"""


def solution(N, number):
    # number가 들어있는 dp 인덱스 = N을 사용한 횟수
    # ex) N = 5일 때
    # dp = [[5], [55], [555], [5555], [55555], [555555], [5555555], [55555555], [555555555]]
    dp = [[]] + [[int(str(N) * i)] for i in range(1, 10)]

    # dp안에 들어있으면 인덱스를 리턴
    if [number] in dp:
        return dp.index([number])

    for i in range(2, 10):
        for j in range(1, i):
            for a in dp[j]:  # N을 j번 사용하여 만들 수 있는 수
                for b in dp[i - j]:  # N을 i - j번 사용하여 만들 수 있는 수
                    dp[i].append(a + b)
                    dp[i].append(a - b)
                    dp[i].append(a * b)
                    if b:
                        dp[i].append(a // b)

        dp[i] = list(set(dp[i]))  # 중복제거
        if number in dp[i]:  # 숫자가 만들어졌다면 종료
            return i

    return -1
