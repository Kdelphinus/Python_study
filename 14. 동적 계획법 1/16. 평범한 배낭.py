"""12865 평범한 배낭"""

num, limit = map(int, input().split())  # 가방에 넣을 수 있는 양, 최대 무게
object_list = [list(map(int, input().split())) for _ in range(num)]  # [무게, 가치]가 저장된 리스트
dp = [[0, 0] for _ in range(num)]  # 현 인덱스에서 가장 높은 가치를 지닌 [무게, 가치]가 저장된 리스트

# 테스트 케이스
# https://www.acmicpc.net/board/view/43538