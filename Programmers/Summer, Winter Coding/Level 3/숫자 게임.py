"""Summer/Winter Coding(~2018)"""


def solution(A, B):
    answer = 0

    # 내림차순 정렬
    A.sort(reverse=True)
    B.sort(reverse=True)

    while B:
        # A의 최솟값이 B의 최솟값보다 작다면 점수를 얻는다
        if A[-1] < B[-1]:
            answer += 1
            A.pop()  # A의 최솟값은 B팀이 이길 수 있을 때만 뺀다
        # B의 최솟값은 이기던, 지던 뺀다
        B.pop()

    return answer
