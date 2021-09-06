def solution(nums):
    answer = 0
    size = len(nums)

    isPrime = [True] * (1000 + 999 + 998 + 1)  # 만들수 있는 최대 숫자인 1000, 999, 998과 인덱스 1 추가

    # 소수인 것은 False로 값을 변경
    for i in range(2, int((1000 + 999 + 998) ** 0.5) + 1):  # 제곱근까지만 확인하면 됨
        for j in range(i + 1, 1000 + 999 + 998 + 1):
            if j % i == 0:
                isPrime[j] = False

    for i in range(size - 2):
        for j in range(i + 1, size - 1):
            for k in range(j + 1, size):
                if isPrime[nums[i] + nums[j] + nums[k]]:
                    answer += 1

    return answer


print(solution([1, 2, 4, 7, 6]))
