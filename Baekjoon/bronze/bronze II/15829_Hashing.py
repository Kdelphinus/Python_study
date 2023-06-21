from string import ascii_lowercase

r = 31
mod = 1234567891
alphabet = {}
for i, s in enumerate(ascii_lowercase):
    alphabet[s] = i + 1

num = int(input())
str = input()
ans = 0
for i, s in enumerate(str):
    ans += alphabet[s] * (r**i)
print(ans % mod)
