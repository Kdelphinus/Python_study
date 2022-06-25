"""9012 괄호"""
import sys

test = int(sys.stdin.readline().rstrip())

for _ in range(test):
    string = list(sys.stdin.readline().rstrip())
    check = 0

    while True:
        if string.pop() == ")":
            check += 1
        else:
            check -= 1

        if check < 0:  # 순서가 잘못 나왔을 경우
            print("NO")
            break

        if not string:
            if check == 0:
                print("YES")
                break
            else:
                print("NO")
                break