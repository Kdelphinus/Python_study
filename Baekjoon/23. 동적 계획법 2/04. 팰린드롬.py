"""10942 팰린드롬"""
import sys

input = sys.stdin.readline


def palindrome(num, numbers, dp):
    """palindrome - i ~ j번째 수열이 팰린드롬인지 판단하는 함수

    Args:
        num (int): 주어진 수열의 길이
        numbers (list): 주어지는 수열
        dp (2d - list): i ~ j번째 수열이 팰린드롬인지 판단하여 dp[i][j]에 1 또는 0을 저장할 리스트
    """
    for i in range(num):  # 길이가 1일 땐 모두 팰린드롬
        dp[i][i] = 1

    for i in range(num - 1):  # 길이가 2일 땐 같아야만 팰린드롬
        if numbers[i] == numbers[i + 1]:
            dp[i][i + 1] = 1

    for end in range(2, num):  # 끝나는 지점
        for start in range(num - end):  # 시작하는 지점
            if (
                numbers[start] == numbers[start + end]  # 첫글자와 끝글자가 같고
                and dp[start + 1][start + end - 1] == 1  # 사이에 있는 글자들이 팰린드롬이라면
            ):
                dp[start][start + end] = 1


num = int(input())  # 수열의 크기
numbers = list(map(int, input().split()))  # 수열

dp = [[0 for _ in range(num)] for i in range(num)]  # dp[i][j]: i ~ j번까지 팰린드롬인가?

order_num = int(input())  # 질문의 개수
orders = [list(map(int, input().split())) for _ in range(order_num)]  # 질문의 내용

palindrome(num, numbers, dp)
for i, j in orders:
    print(dp[i - 1][j - 1])  # 명령은 1부터 시작이나 인덱스는 0부터 시작이므로
