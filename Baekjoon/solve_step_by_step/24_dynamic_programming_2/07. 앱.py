"""7579 앱"""
# import sys

# input = sys.stdin.readline


# def optimization(num, memory, current_memory, value):
#    """optimization: 최적화해주는 함수

#    Args:
#        num (int): 현재 실행 중인 앱의 개수
#        memory (int): 확보해야 할 메모리
#        current_memory (list): 현재 실행 중인 앱의 메모리가 저장된 리스트
#        value (list): 현재 실행 중인 앱을 재실행할 때 필요한 비용이 저장된 리스트

#    Returns:
#        dp[memory] (int): memory를 확보하기 위한 앱 비활성화의 최소 비용
#    """
#    dp = [sum(value) for _ in range(memory + 1)]  # 모든 앱을 비활성화할 경우를 초기값으로 설정

#    for i in range(num):
#        for j in range(memory, -1, -1):
#            if current_memory[i] < j:  # 현재 메모리가 확보할 메모리보다 작다면
#                dp[j] = min(
#                    dp[j], dp[j - current_memory[i]] + value[i]
#                )  # 현재 구해진 값과 지금 메모리를 비활성화 하여 메모리를 얻는 것 중 작은 것을 저장
#            else:  # 현재 메모리가 확보할 메모리보다 같거나 크다면
#                dp[j] = min(dp[j], value[i])  # 현재 메모리의 비용과 저장된 비용 중 작은 것을 저장

#    return dp[memory]


# num, memory = map(int, input().split())  # 현재 켜져있는 앱의 수, 필요한 메모리
# current_memory = list(map(int, input().split()))  # 현재 켜져있는 앱의 메모리
# value = list(map(int, input().split()))  # 현재 켜져있는 앱이 다시 실행할 때 추가적으로 드는 비용


# print(optimization(num, memory, current_memory, value))


# ------------------------------------------------------------------------------------------------------------
"""다른 답안(시간이 훨씬 절약됨)"""
"""링크: https://claude-u.tistory.com/445"""
import sys

input = sys.stdin.readline


def optimization(num, memory, bytes, costs):
    """optimization 필요한 메모리를 최소 비용으로 얻는 함수

    Args:
        num (int): 실행 중인 앱의 개수
        memory (int): 필요한 메모리
        bytes (list): 실행 중인 앱이 사용하는 메모리가 저장된 리스트
        costs (list): 실행 중인 앱을 재실행할 때 필요한 비용이 저장된 리스트
        dp[i][j] (2d-list): i번째 앱까지 중 j cost로 얻을 수 있는 최대 byte

    Returns:
        result (int): 필요한 메모리를 얻을 수 있는 최소 비용
    """
    dp = [[0 for _ in range(sum(costs) + 1)] for _ in range(num + 1)]
    result = sum(costs)

    for i in range(num + 1):
        byte = bytes[i]
        cost = costs[i]

        for j in range(1, sum(costs) + 1):
            if j < cost:  # 현재 앱을 비활성화할만큼의 cost가 충분하지 않을 경우
                dp[i][j] = dp[i - 1][j]
            else:  # 같은 cost 내에서 현재 앱을 끈 뒤의 byte와 현재 앱을 끄지 않은 뒤의 byte를 비교
                dp[i][j] = max(byte + dp[i - 1][j - cost], dp[i - 1][j])

            if dp[i][j] >= memory:  # 조건이 충족된다면
                result = min(result, j)  # 더 작은 cost로 갱신

    for i in dp:
        print(*i)
    return result


N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))  # byte
C = [0] + list(map(int, input().split()))  # cost
print(optimization(N, M, A, C))
