MOD = 1000000007
num = int(input())

# 1부터 num까지 3제곱한 값을 모두 더한 것은 (num*(num+1) / 2)^2과 같다
anw = (((num * (num + 1) // 2) % MOD) ** 2) % MOD
print(anw)
