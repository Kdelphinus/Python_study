R, C, N = map(int, input().split())
h, w = R // N, C // N
if R % N:
    h += 1
if C % N:
    w += 1
print(h * w)
