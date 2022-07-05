"""1932 정수 삼각형"""

n = int(input())  # 삼각형 크기
triangle = [list(map(int, input().split())) for _ in range(n)]  # 삼각형을 입력 받는다

# 가장 밑에서 두 번째 행부터 계산
# 밑에 있는 두 숫자 중 큰 숫자와 더함
# 이를 계속 반복
for i in range(n - 2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] = (
            max(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
        )

# 맨 위에 있는 수는 자연스레 최댓값이 됨
print(triangle[0][0])
