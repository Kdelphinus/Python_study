# 답안: https://whwl.tistory.com/93
# 백준 3663번 문제와 비슷(조건이 다름)
# 논란이 많은 문제


def solution(name):
    # 알파벳 바꾸기
    change = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    idx = 0  # 현 위치
    answer = 0  # 커서를 누른 횟수

    while True:
        answer += change[idx]  # 현재 위치 알파벳을 바꾸고
        change[idx] = 0  # 바꿈으로 표시

        if sum(change) == 0:  # 모든 알파벳을 다 바꾸면 종료
            return answer

        left, right = 1, 1
        while change[idx - left] == 0:  # 안 바꾼 것이 나올때까지 왼쪽으로 이동
            left += 1
        while change[idx + right] == 0:  # 안 바꾼 것이 나올때까지 오른쪽으로 이동
            right += 1

        # 왼쪽과 오른쪽 중, 더 가까운 방향으로 이동
        # 문제에서 처음 위치에서 끝 위치는 갈 수 있으나 끝에서 처음으로 갈 수는 없음으로 조건이 걸림
        # 그렇기에 오른쪽, 왼쪽 선택지의 거리가 같을 땐, 오른쪽으로 이동해야 함
        answer += left if left < right else right
        idx += -left if left < right else right


test = int(input())
for _ in range(test):
    name = input()
    print(solution(name))
