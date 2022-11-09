people, area = map(int, input().split())
people *= area
for i in list(map(int, input().split())):
    print(i - people, end=" ")
