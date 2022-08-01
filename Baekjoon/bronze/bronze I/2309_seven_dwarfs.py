dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))
over = sum(dwarfs) - 100
for i in range(9):
    for j in range(i + 1, 9):
        if dwarfs[i] + dwarfs[j] == over:
            del dwarfs[j]
            del dwarfs[i]
            break
    if len(dwarfs) == 7:
        break
dwarfs.sort()
for d in dwarfs:
    print(d)
