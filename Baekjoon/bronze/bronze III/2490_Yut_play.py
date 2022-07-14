move = ["E", "A", "B", "C", "D"]
for _ in range(3):
    yut = list(map(int, input().split()))
    zero = 0
    for y in yut:
        if y == 0:
            zero += 1
    print(move[zero])
