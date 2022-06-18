num = int(input())
member = []
for _ in range(num):
    name, day, month, year = input().split()
    member.append([name, int(day), int(month), int(year)])
member.sort(key=lambda x: (x[3], x[2], x[1]))
print(member[-1][0])
print(member[0][0])
