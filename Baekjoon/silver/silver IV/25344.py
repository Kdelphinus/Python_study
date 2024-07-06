def gcd(a: int, b: int) -> int:
    return gcd(b, a % b) if b else a


n = int(input())
lst = list(map(int, input().split()))
num1 = lst.pop()

while lst:
    num2 = lst.pop()
    great = gcd(num1, num2)
    num1 = (num1 * num2) // great

print(num1)
