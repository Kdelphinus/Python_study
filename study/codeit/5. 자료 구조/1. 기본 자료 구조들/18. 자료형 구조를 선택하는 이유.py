# 예시를 위해 사용할 모듈 import
import time

# 데이터를 리스트에 저장한다
test_list = [x for x in range(0, 1000000)]

# 특정 항목이 리스트에 있는지 확인할 때 걸리는 시간 파악
t_0 = time.time()
999999 in test_list  # 리스트 탐색
t_1 = time.time()

print(f"리스트에서 특정 항목을 찾는데 걸린 시간: {t_1 - t_0}")

# 데이터를 set에 저장한다
test_set = set([x for x in range(0, 1000000)])

# 특정 항목이 set에 있는지 확인할 때 걸리는 시간 파악
t_2 = time.time()
999999 in test_set
t_3 = time.time()

print(f"set에서 특정 항목을 찾는데 걸린 시간: {t_3 - t_2}")

""" 이 차이는 리스트를 구현하는 동적 배열에선 탐색이 O(n)이지만
    set를 구현하는 해시 테이블에선 탐색이 O(1)이기 때문이다 """