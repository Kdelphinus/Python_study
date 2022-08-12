n1, n2 = input().strip().split()
n1, n2 = n1[::-1], n2[::-1]
print(int(str(int(n1) + int(n2))[::-1]))


# 함수를 만들어 사용하는게 조금 더 빠르다
def rev(num: str):
    return int(num[::-1])


n1, n2 = input().strip().split()
print(rev(str(rev(n1) + rev(n2))))
