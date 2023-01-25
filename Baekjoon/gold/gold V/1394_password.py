MOD = 900528

alphabet = input()
alpha_idx = {}
for idx, a in enumerate(alphabet):
	alpha_idx[a] = idx + 1

pw = input()
length = len(alphabet)
n = 1
ans = 0
for p in pw[::-1]:
	ans = (ans + (n * alpha_idx[p]))
	n = (n * length) % MOD

print(ans % MOD)