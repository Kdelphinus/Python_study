"""10986 나머지 합 / gold III"""
# 링크: https://velog.io/@learningssik/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-10986-%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""
m으로 나눴을 때, 나머지가 같은 부분합을 빼면 그 결과는 m의 배수가 나온다.
그렇기에 같은 나머지를 가진 부분합끼리의 쌍의 개수를 구하면 된다.
"""


import sys

input = sys.stdin.readline

cnt = 0
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
presum = 0
prefix = [0] * m
"""
나머지가 0인 부분은 자기 자신도 m의 배수이다.
그렇기에 0을 추가해서 본인만 만들어지는 부분도 감안한다.
"""
prefix[0] = 1
for number in numbers:
    presum += number
    prefix[presum % m] += 1

# 두 쌍을 뽑는 과정
for r in prefix:
    cnt += (r * (r - 1)) // 2
print(cnt)


#######################################################################
"""시간 초과"""

# cnt = 0
# n, m = map(int, input().split())
# numbers = list(map(int, input().split()))
# remainder = [0]
# for number in numbers:
#     remainder.append(number + remainder[-1])
#
# for i in range(n):
#     for j in range(i + 1, n + 1):
#         if (remainder[j] - remainder[i]) % m == 0:
#             cnt += 1
# print(cnt)
