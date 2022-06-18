test = int(input())
for t in range(test):
    num = int(input())
    name, price = "", 0
    for _ in range(num):
        tmp_p, tmp_n = input().split()
        if int(tmp_p) > price:
            price = int(tmp_p)
            name = tmp_n
    print(name)
