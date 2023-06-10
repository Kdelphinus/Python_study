stick = sorted(list(map(int, input().split())))
if stick[2] < stick[1] + stick[0]:
    print(sum(stick))
else:
    print((stick[1] + stick[0]) * 2 - 1)
