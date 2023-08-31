def cal_time(h, m, t):
	m += t
	if m > 59:
		h += m // 60
		m %= 60
	if h > 23:
		h -= 24
	return h, m


N = int(input())
T, M = map(int, input().split())
for _ in range(N):
	c = int(input())
	T, M = cal_time(T, M, c)
print(T, M)
