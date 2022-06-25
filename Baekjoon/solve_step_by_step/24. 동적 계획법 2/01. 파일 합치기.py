"""11066 파일 합치기"""
import sys
import math

input = sys.stdin.readline


def merge_page():
    # 장의 개수와 각 장의 크기
    num, pages = int(input()), list(map(int, input().split()))

    # 누적 합계
    running_total = [0] * (num + 1)
    for i in range(num):
        running_total[i] = running_total[i - 1] + pages[i]

    # dp[start][end]: start에서 end까지 합치는데 필요한 최소 비용
    dp = [[0 for i in range(num)] for _ in range(num)]
    for gap in range(1, num):  # gap: 시작 페이지와 끝 페이지 사이 간격
        for start in range(num - gap):  # start: 시작 페이지
            end = start + gap  # end: 끝 페이지

            dp[start][end] = math.inf  # 초기값은 무한으로 지정
            for i in range(start, end):  # i: 합치는 부분,
                dp[start][end] = min(
                    dp[start][end],
                    dp[start][i]
                    + dp[i + 1][end]
                    + running_total[end]
                    - running_total[start - 1],
                )

    print(dp[0][-1])


test = int(input())

for _ in range(test):
    merge_page()


""" 해설 참고
https://data-make.tistory.com/402 [Data Makes Our Future] 
https://m.post.naver.com/viewer/postView.nhn?volumeNo=28894924&memberNo=33264526"""
