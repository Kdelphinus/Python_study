"""9019 DSLR"""
"""시간 초과를 피하기 위해 pypy3로 제출"""
import sys
from collections import deque

input = sys.stdin.readline


def R_order(now):
    """R_order 오른쪽으로 회전시키는 함수

    Args:
        now (int): 회전시킬 수

    Returns:
        (int): 오른쪽으로 회전한 수
    """
    tmp = str(now).zfill(4)  # 레지스트리는 항상 4자리
    return int(tmp[3] + tmp[:3])


def L_order(now):
    """L_order 왼쪽으로 회전시키는 함수

    Args:
        now (int): 회전시킬 수

    Returns:
        (int): 왼쪽으로 회전한 수
    """
    tmp = str(now).zfill(4)  # 레지스트리는 항상 4자리
    return int(tmp[1:] + tmp[0])


def DSLR(initial, final):
    """DSLR initial -> final로 가는 최단 명령을 찾는 함수

    Args:
        initial (int): 초기값
        final (int): 최종값

    Returns:
        (str): 최단 명령어
    """
    dp = [[] for _ in range(10000)]  # [이전 위치, 명령어]
    dp[initial] = [-1, ""]  # 초기는 이전 위치가 없고 명령어도 없다
    queue = deque()
    queue.append(initial)
    while queue:
        now = queue.popleft()
        if now == final:  # 최종값에 도달했을 때
            string = f"{dp[now][1]}"  # 현재 명령어 추가
            tmp = dp[now][0]
            while True:  # 초기값이 나올 때까지 명령어 추가
                if tmp == initial:  # 초기값까지 도달하면 종료
                    return string[::-1]

                string += dp[tmp][1]
                tmp = dp[tmp][0]

        # D: 2배, S: 하나 작은 값, L: 왼쪽으로 돌린 수, R: 오른쪽으로 돌린 수
        D, S, L, R = now * 2, now - 1, L_order(now), R_order(now)
        if D >= 10000:  # 4자리를 넘어가면 10000으로 나눈 나머지를 값으로 가짐
            D %= 10000
        if S < 0:  # 음수로 가면 9999로 초기화
            S = 9999

        # 아직 탐색하지 않은 값이 나왔을 때만 추가
        # [이전 위치, 현재 명령어]
        if not dp[D]:
            queue.append(D)
            dp[D] = [now, "D"]

        if not dp[S]:
            queue.append(S)
            dp[S] = [now, "S"]

        if not dp[L]:
            queue.append(L)
            dp[L] = [now, "L"]

        if not dp[R]:
            queue.append(R)
            dp[R] = [now, "R"]


test = int(input())
for t in range(test):
    initial, final = map(int, input().split())
    print(DSLR(initial, final))

# ----------------------------------------------------------------------------

"""다른 답안(내 답안에 비해 1/3 시간 단축)
링크: https://pacific-ocean.tistory.com/388"""
"""시간 초과를 피하기 위해 pypy3로 제출"""
from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    """명령어를 저장해가며 구하는 방식"""
    q = deque()
    q.append([a, ""])
    while q:
        number, result = q.popleft()
        dn = (number * 2) % 10000  # 10000으로 나눈 나머지를 사용
        if dn == b:  # 답이 나왔다면 명령어 추가하고 리턴
            return result + "D"
        elif arr[dn] == 0:  # 아직 탐색하지 않은 숫자이면 탐색
            arr[dn] = 1
            q.append([dn, result + "D"])  # 현재 숫자와 명령어
        sn = number - 1 if number != 0 else 9999  # 0은 1을 빼면 음수가 되므로 9999로 초기화
        if sn == b:  # 답이 나왔다면 명령어 추가하고 리턴
            return result + "S"
        elif arr[sn] == 0:  # 아직 탐색하지 않은 숫자이면 탐색
            arr[sn] = 1
            q.append([sn, result + "S"])
        ln = int(number % 1000 * 10 + number / 1000)
        if ln == b:  # 답이 나왔다면 명령어 추가하고 리턴
            return result + "L"
        elif arr[ln] == 0:  # 아직 탐색하지 않은 숫자이면 탐색
            arr[ln] = 1
            q.append([ln, result + "L"])
        rn = int(number % 10 * 1000 + number // 10)
        if rn == b:  # 답이 나왔다면 명령어 추가하고 리턴
            return result + "R"
        elif arr[rn] == 0:  # 아직 탐색하지 않은 숫자이면 탐색
            arr[rn] = 1
            q.append([rn, result + "R"])


t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    arr = [0 for i in range(10000)]
    print(bfs())
