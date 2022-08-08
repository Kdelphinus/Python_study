w, k = [], []
for _ in range(10):
    w.append(int(input()))
for _ in range(10):
    k.append(int(input()))
w.sort()
k.sort()
print(f"{sum(w[7:])} {sum(k[7:])}")
