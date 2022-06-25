"""1181 단어 정렬"""

n = int(input())
temp = []

for _ in range(n):
    tem = input()
    if tem not in temp:
        temp.append(tem)

temp.sort(key=lambda x: (len(x), x))

for i in temp:
    print(i)