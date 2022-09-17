"""
xor은 비트 논리 연산자 중 하나로 서로 두 개의 수가 다르면 1, 같으면 0을 리턴한다.
ex) 0b1101 ^ 0b1001 = 0b100

0 ~ n까지 앞에서부터 두개씩 짝지어 xor을 하면 1이 나온다.
예를 들어 n=6이면

0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6
= (0 ^ 1) ^ (2 ^ 3) ^ (4 ^ 5) ^ 6
= 1 ^ 1 ^ 1 ^ 6
= 1 ^ 6

이 나온다. 

또한 a ~ b까지 xor 연산의 결과는 (0 ~ b까지 xor 연산) ^ (0 ~ a -1까지 xor 연산)과 동일하다.
즉, 부분합으로 구할 수 있다. 
"""


def xor(num):
    if num % 2 == 0:  # num이 짝수면 1의 개수에 따라 num 또는 1 ^ num으로 나온다.
        return int(bin(num ^ 1), 2) if (num // 2) % 2 == 1 else num
    else:  # num이 홀수면 1의 개수에 따라 1 또는 0이 나온다.
        return 1 if ((num + 1) // 2) % 2 == 1 else 0


a, b = map(int, input().split())
if a == b:
    print(a)
else:
    print(int(bin(xor(a - 1) ^ xor(b)), 2))
