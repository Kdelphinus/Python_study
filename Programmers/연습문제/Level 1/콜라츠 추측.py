def solution(num):
    cnt = 0
    if num == 1:
        return 0

    while True:
        if num % 2:
            num *= 3
            num += 1
        else:
            num /= 2
        cnt += 1

        if num == 1:
            return cnt

        if cnt > 500:
            return -1
