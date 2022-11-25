num = sorted(list(map(int, input().split())))
orders = input()
for o in orders:
    if o == "A":
        print(num[0], end=" ")
    elif o == "B":
        print(num[1], end=" ")
    else:
        print(num[2], end=" ")
