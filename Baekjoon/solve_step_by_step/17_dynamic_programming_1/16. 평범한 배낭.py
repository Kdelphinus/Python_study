"""12865 평범한 배낭"""

weights = []  # 무게를 담을 리스트
values = []  # 가치를 담을 리스트
num, limit = map(int, input().split())  # 가방에 넣을 수 있는 양, 최대 무게
for _ in range(num):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

dp = [0 for _ in range(limit + 1)]  #  최대 용량이 인덱스만큼 일 때 넣을 수 있는 최대 가치값이 저장된 리스트

for i in range(num):
    for j in range(limit, 0, -1):  # 무게 제한이 가장 큰 것부터 살펴본다
        if weights[i] <= j:  # 물건이 가방에 들어갈 수 있으면
            dp[j] = max(
                dp[j], dp[j - weights[i]] + values[i]
            )  # 물건을 안 넣었을 때 가치 vs 물건을 넣고 더 담을 수 있는 물건 가치의 총합

print(dp[limit])
