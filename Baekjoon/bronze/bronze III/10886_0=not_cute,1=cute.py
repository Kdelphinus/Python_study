num = int(input())
zero, one = 0, 0
for _ in range(num):
    vote = input()
    if vote == "0":
        zero += 1
    elif vote == "1":
        one += 1
print("Junhee is not cute!" if zero > one else "Junhee is cute!")
