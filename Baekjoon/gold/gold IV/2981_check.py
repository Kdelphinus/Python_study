# 해설은 단계별로 풀기 15단계, 검문 문제 참고


def gcd(a: int, b: int) -> int:
    if a < b:
        tmp = b
        b = a
        a = tmp
    return gcd(b, a % b) if b else a


n = int(input())
n1 = int(input())
n2 = int(input())
min_gcd = abs(n1 - n2)
for _ in range(n - 2):
    n1 = n2
    n2 = int(input())
    min_gcd = gcd(min_gcd, abs(n2 - n1))
divisor = []
for i in range(2, int(min_gcd**0.5) + 1):
    if min_gcd % i == 0:
        divisor.append(i)
        divisor.append(min_gcd // i)
divisor.append(min_gcd)
print(*sorted(list(set(divisor))))
