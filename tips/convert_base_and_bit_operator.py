"""
2진수: 0b
8진수: 0o
16진수: 0x
"""

"""다른 진수의 형태로 표현하려면 접두어를 붙여야 한다"""
print(42 == 0b101010)  # True
print(42 == 0o52)  # True
print(42 == 0x2A)  # True


"""십진수를 다른 진수의 문자열로 변환"""
print(bin(42))  # 0b101010, 2진수
print(oct(42))  # 0o52, 8진수
print(hex(42))  # 0x2a, 16진수

# 다른 진수를 사용해도 결과는 같다
print(bin(0b101010))  # 0b101010, 2진수
print(oct(0b101010))  # 0o52, 8진수
print(hex(0b101010))  # 0x2a, 16진수
print(str(0b101010))  # '42', 10진수


"""다른 진수의 문자열을 숫자형으로 변환"""
print(int("0b101010", 2))  # 42
print(int("0o52", 8))  # 42
print(int("0x2a", 16))  # 42
print(int("42", 10))  # 42, int는 10이 디폴트값이기에 10진수로 변환되는 것


"""접두어 제외 & 포함하기"""
print(format(42, "b"))  # '101010', 2진수
print(format(42, "o"))  # '52', 8진수
print(format(42, "x"))  # '2a', 16진수
print(format(42, "X"))  # '2A', 16진수
print(format(42, "d"))  # '42', 10진수

print(format(42, "#b"))  # '0b101010', 2진수
print(format(42, "#o"))  # '0o52', 8진수
print(format(42, "#x"))  # '0x2a', 16진수
print(format(42, "#X"))  # '0x2A', 16진수
print(format(42, "#d"))  # '42', 10진수


"""10진수 -> n진수"""
import string

# 숫자와 소문자 알파벳 조합
temp = string.digits + string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)  # q: num // base, r: num % base
    if q:
        return convert(q, base) + temp[r]
    else:
        return temp[r]


print(convert(10, 2))  # 1010
print(convert(10, 4))  # 22
print(convert(10, 6))  # 14
print(convert(10, 8))  # 12
print(convert(10, 12))  # a


"""n진수 -> n진수"""
# 정확히는 n진수 -> 10진수 -> n진수
print(convert(int("a", 16), 2))  # 1010
print(convert(int("4", 5), 3))  # 11


"""비트 논리 연산자"""
print(bin(0b1101 & 0b1001))  # 0b1001, 1과 1만 1, 나머지 조합은 모두 0
print(bin(0b1101 | 0b1001))  # 0b1101, 0과 0만 0, 나머지 조합은 모두 1
print(bin(0b1101 ^ 0b1001))  # 0b100, 서로 두 개의 수가 다를 때 1, 같으면 0
print(bin(~0b1101))  # -0b1110, 반대로

# ~의 예시
print(int(0b1101), int(-0b1110))  # 13, -14
print(int(0b11), int(-0b100))  # 3, -4

# 10진수를 넣어도 자동으로 비트로 바꾸어 연산
print(~13)  # -14
print(4 & 5)  # 4, 4 & 5 == 0b100 == 4
print(bin(4), bin(5))  # 0b100 0b101


"""시프트 연산자"""
print(0b0011 << 2)  # 12, 왼쪽으로 2번 이동
print(bin(12))  # 0b1100

print(0b1100 >> 2)  # 3, 오른쪾으로 2번 이동
print(bin(3))  # 0b11

print(0b1100 >> 4)  # 0, 1이 더이상 넘어갈 곳이 없으면 사라진다
print(bin(0))  # 0b0

print(0b1100 << 2)  # 48
print(bin(48))  # 0b110000
