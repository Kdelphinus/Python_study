"""1003 피보나치 함수"""

test = int(input())

for _ in range(test):
    num = int(input())

    def fibo_cnt(num):
        """Tabulation 방식으로 수열을 구함"""
        zero_call = [1, 0]
        one_call = [0, 1]

        for i in range(2, num + 1):
            zero_call.append(zero_call[i - 2] + zero_call[i - 1])
            one_call.append(one_call[i - 2] + one_call[i - 1])

        return [zero_call[num], one_call[num]]

    print(*fibo_cnt(num))
