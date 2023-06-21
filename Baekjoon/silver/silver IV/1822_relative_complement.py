an, bn = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
RC = A - B
print(len(RC))
print(*sorted(list(RC)))
