""" 11653 소인수분해 """

n = int(input())
i = 2

if n > 1:
    while n != 1:
        if n % i == 0:
            print(i)
            n //= i
        else:
            i += 1
