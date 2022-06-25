"""1654 랜선 자르기"""
import sys

input = sys.stdin.readline
long_cable = 1  # 자른 케이블의 가장 긴 길이


def lan_cable_divide(start, end, num, k_list):
    """start ~ end 사이에서 num개의 랜선을 만들 수 있는 최댓값을 구하는 함수"""
    global long_cable

    if start > end:
        return

    total = 0  # 잘랐을 때 나오는 케이블 개수

    mid = (start + end) // 2
    for k in k_list:
        total += k // mid

    if total >= num:  # 케이블 개수 이상으로 케이블이 나오면 더 큰 수가 있는 지 확인
        if long_cable < mid:  # 이전에 구한 값보다 크다면
            long_cable = mid
        return lan_cable_divide(mid + 1, end, num, k_list)
    else:  # 케이블 개수 미만으로 케이블이 나오면 더 작은 수에서 확인
        return lan_cable_divide(start, mid - 1, num, k_list)


k, num = map(int, input().split())  # 가지고 있는 랜선, 필요한 랜선
k_list = [int(input()) for _ in range(k)]  # 가지고 있는 랜선의 길이들
lan_cable_divide(
    2, max(k_list), num, k_list
)  # 굳이 가장 짧은 랜선을 쓰지 않아도 원하는 개수만큼 구할 수 있기에 최댓값까지 확인해주어야 함
print(long_cable)
