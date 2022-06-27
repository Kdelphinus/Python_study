"""24416 알고리즘 수업 - 피보나치 수 1 / 브론즈 I"""

n = int(input())
f = [1, 1]
for _ in range(n - 2):
    x = f[0] + f[1]
    f[0], f[1] = f[1], x
print(f[1], n - 2)
