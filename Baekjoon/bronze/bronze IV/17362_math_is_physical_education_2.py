n = int(input())
if n % 8 == 1:
    print(1)
elif n % 8 == 2 or n % 8 == 0:
    print(2)
elif n % 8 == 3 or n % 8 == 7:
    print(3)
elif n % 8 == 4 or n % 8 == 6:
    print(4)
else:
    print(5)
