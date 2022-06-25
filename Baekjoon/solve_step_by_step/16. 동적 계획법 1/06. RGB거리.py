"""1149 RGB거리"""

num = int(input())
prices = [
    list(map(int, input().split())) for _ in range(num)
]  # 각 집마다 색칠하는 비용(R, G, B 순서)

# i번째 색을 정했을 때, i - 1번째 색 중 가장 낮은 가격을 더해준다
for i in range(1, len(prices)):
    prices[i][0] = min(prices[i - 1][1], prices[i - 1][2]) + prices[i][0]
    prices[i][1] = min(prices[i - 1][0], prices[i - 1][2]) + prices[i][1]
    prices[i][2] = min(prices[i - 1][1], prices[i - 1][0]) + prices[i][2]

# 색칠한 세 가지 방법 중 가장 작은 가격을 출력한다
print(min(prices[num - 1][0], prices[num - 1][1], prices[num - 1][2]))
