# 풀이: subinlee and https://pacific-ocean.tistory.com/240
def count_num(n: int) -> list:
    digit = [0 for _ in range(10)]

    place = 1
    while n:
        # 일의 자리수가 9가 될때까지 직접 세기
        while n % 10 != 9:
            for i in str(n):
                digit[int(i)] += place
            n -= 1
        # n이 한 자리수거나 -1이라면(위 코드가 1 ~ 8은 -1로 만듬) 직접 세고 종료
        if n < 10:
            for i in range(n + 1): # 여기서 0의 개수를 안 구해도 위에서 -1이 되어서 온 숫자는 이미 0이 포함되어있다.
                digit[i] += place
            digit[0] -= place # 여기서도 0의 개수를 세기 때문에 빼줘야 함
            break
        n //= 10
        # 끝자리가 9일 때는 10으로 나눈 몫 + 1만큼 나타난다.
        # 이때, 자릿수마다 숫자를 계산하기 위해 place를 이용한다.
        for i in range(10):
            digit[i] += (n + 1) * place
        # 0이 계속해서 자릿수만큼 더해지고 있으므로 빼준다.
        digit[0] -= place
        place *= 10

    return digit


if __name__ == "__main__":
    num = int(input())
    print(*count_num(num))
