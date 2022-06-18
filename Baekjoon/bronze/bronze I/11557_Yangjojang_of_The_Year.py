test = int(input())
for t in range(test):
    num = int(input())
    univ, drink = "", 0
    for _ in range(num):
        tmp1, tmp2 = input().split()
        if drink < int(tmp2):
            univ = tmp1
            drink = int(tmp2)
    print(univ)
