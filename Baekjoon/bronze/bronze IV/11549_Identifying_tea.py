from collections import Counter

T = int(input())
print(Counter(list(map(int, input().split())))[T])
