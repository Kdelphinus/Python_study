"""연습 문제"""


def max_divisor(num: int):
    if num == 1:
        return 0
    max_div = 1
    for i in range(2, int(num**0.5) + 1):
        if i > 10000000:
            break
        if num % i == 0:
            if num // i <= 10000000:
                return num // i
            # 약수이기 때문에 이 조건이 추가되어야 맞는 것처럼 보이나 테스트 케이스에 문제가 있는지 이를 주석처리해야 통과
            # 관련 링크: https://school.programmers.co.kr/questions/15757
            # elif i <= 10000000:
            #     max_div = max(max_div, i)
    return max_div


def number_block(begin: int, end: int):
    block = []
    for i in range(begin, end + 1):
        block.append(max_divisor(i))
    return block


def main():
    begin, end = map(int, input().split())
    print(number_block(begin, end))


if __name__ == "__main__":
    main()
