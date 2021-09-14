"""9461 파도반 수열"""


def padovan(num):
    # base case
    prev_1 = 1
    prev_2 = 1
    current = 1

    # 계산 과정
    for i in range(4, num + 1):
        temp = current
        current = prev_1 + prev_2  # padovan[i]번째
        prev_1 = prev_2  # padovan[i - 2]번째
        prev_2 = temp  # padovan[i - 1]번째

    return current


test = int(input())

for _ in range(test):
    num = int(input())
    print(padovan(num))