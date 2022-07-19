from collections import Counter

number = []
for _ in range(10):
    tmp = int(input())
    number.append(tmp)

print(sum(number) // 10)
print(Counter(number).most_common()[0][0])
