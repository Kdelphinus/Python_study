"""11051 이항 계수 2"""

# 부동소수점때문에 직접 구현한 factorial은 숫자가 커질수록 오차가 커짐
# 그렇기에 math 모듈에 내장된 factorial함수를 가져옴
from math import factorial

num, k = map(int, input().split())  # 이항계수 (num, k)가 주어짐
result = factorial(num) // (factorial(k) * factorial(num - k))
print(result % 10007)


# --------------------------------------------------------------------------------------------------
# 파스칼의 삼각형을 이용하여 푼 방법
# 파스칼 삼각형은 맨 왼쪽과 오른쪽은 모두 1이고 나머지는 두 대각선 위에 있는 값을 더한 값을 갖는 삼각형
n, k = map(int, input().split())
d = []

for i in range(n + 1):
    d.append([1] * (i + 1))

for i in range(2, n + 1):
    for j in range(1, i):
        d[i][j] = (d[i - 1][j - 1] + d[i - 1][j]) % 10007

print(d[n][k])
