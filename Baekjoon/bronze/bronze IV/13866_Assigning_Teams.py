s = sorted(list(map(int, input().split())))
print(abs(s[0] + s[-1] - s[1] - s[2]))
