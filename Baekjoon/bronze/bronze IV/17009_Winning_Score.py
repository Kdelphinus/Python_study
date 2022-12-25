a, b = 0, 0
a += int(input()) * 3
a += int(input()) * 2
a += int(input())
b += int(input()) * 3
b += int(input()) * 2
b += int(input())

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("T")
