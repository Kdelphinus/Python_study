n = int(input())
cnt = 0
while n >= 4:
    n -= 1
    cnt += 1
if cnt % 2:
    print("CY") if n % 2 else print("SK")
else:
    print("SK") if n % 2 else print("CY")

##########################################################

"""
돌을 고를 수 있는 경우는 무조건 홀수개이다. 그렇기에 짝수개이면 무조건 한 개가 남고 홀수개이면 남는 것이 없게 된다.
따라서 먼저 고르는 상근이는 홀수개일때, 창영이는 짝수개일때 무조건 이길 수 있다.
"""

n = int(input())
print("SK" if n % 2 else "CY")
