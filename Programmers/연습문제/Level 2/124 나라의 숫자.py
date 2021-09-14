# 나의 풀이
# 앞자리부터 차례대로 찾는 방식
def solution(n):
    answer = ""
    cnt = 1
    num_list = ["1", "2", "4"]
    num = 0

    while True:  # 1, 2, 4를 사용한 수로 바꾸었을 때, 숫자의 길이를 구함
        num += 3 ** cnt  # 한 자리당 3개씩 숫자가 들어갈 수 있기에 3의 제곱수로 개수가 증가
        if n <= num:  # n을 넘어가면 종료
            break
        cnt += 1
    num -= 3 ** cnt  # n과 같은 길이의 숫자는 그 전 제곱수
    n -= num + 1  # 그 자릿수에서 몇번째 숫자인지 구함(0번째부터 시작)
    tmp = cnt

    for _ in range(tmp):  # 전체 범위를 3분할하여 현재 위치가 어디에 포함되는지 찾는 것을 자릿수만큼 반복
        cnt -= 1
        divider = 3 ** cnt  # 현재 개수보다 한 단계 작은 3의 제곱수
        answer += num_list[n // divider]  # 위치를 3분할하여 무슨 숫자가 들어갈지 찾음
        n %= divider  # 3분할 한 곳에서 위치를 구함

    return answer


n = int(input())
print(solution(n))

# -------------------------------------------------------------------------------------

# 최다 추천 풀이
# 뒷자리(일의 자리)부터 찾는 방식
# 훨씬 간편
def change124(n):
    num = ["1", "2", "4"]
    answer = ""

    while n > 0:
        n -= 1  # 0번째 시작으로 바꾸기 위해
        answer = num[n % 3] + answer  # 가장 작은 범위부터 3분할
        n //= 3

    return answer
