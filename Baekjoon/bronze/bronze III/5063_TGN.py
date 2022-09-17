t = int(input())
for _ in range(t):
    non, ad, price = map(int, input().split())
    if non == ad - price:
        print("does not matter")
    elif non > ad - price:
        print("do not advertise")
    else:
        print("advertise")
