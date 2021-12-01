num = int(input())

# 9의 배수는 자릿수의 합이 항상 9의 배수
# 6!부터 9의 배수이므로 6이상의 수는 모두 9가 된다
if num >= 6:
    print(9)
else:
    fact = 1
    for i in range(2, num + 1):
        fact *= i

    while True:
        tmp = 0
        while fact > 0:
            tmp += fact % 10
            fact //= 10

        if len(str(tmp)) == 1:
            print(tmp)
            break

        fact = tmp
