s = {1, 2, 3, 4, 5, 6}

"""차집합, 교집합, 합집합"""
a = {5, 6}
print(s - a)  # {1, 2, 3, 4}, 차집합
print(s & a)  # {5, 6}, 교집합
print(s | a)  # {1, 2, 3, 4, 5, 6, 7}, 합집합


"""여러 기능들"""
s.add(7)  # 새로운 값 추가
s.remove(7)  # 값 삭제, 없으면 에러
s.discard(7)  # 값 삭제, 없으면 무시하고 진행
print(s.pop())  # 1, 임의의 값을(지금 파일 상에선 맨 앞 값) 리턴 후, 삭제

cs = s.copy()  # 집합 복사
print(cs)  # {2, 3, 4, 5, 6}

cs.clear()  # 집합 비우기
print(cs)  # set()


"""두 집합 비교, bool 리턴"""
print(s.isdisjoint(a))  # False, 두 집합이 공통 원소를 갖지 않는가?
print(s.issubset(a))  # False, s가 a의 부분집합인가?
print(s.issuperset(a))  # True, s가 a의 확대집합인가?


"""여러 집합 만들기"""
s1 = {1, 2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9}

# 합집합
print(s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}, 합집합 리턴

print(s1)  # {1, 2, 3, 4, 5, 6}
s1.update(s2)  # 원본값을 합집합으로 변경
print(s1)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}


# 차집합
print(s1.difference(s2))  # {1, 2, 3, 4, 5}, 차집합 리턴

print(s1)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
s1.difference_update(s2)  # 원본값을 차집합으로 변경
print(s1)  # {1, 2, 3, 4}


# 교집합
s1 = {1, 2, 3, 4, 5, 6}
print(s1.intersection(s2))  # {5, 6}, 교집합 리턴

print(s1)  # {1, 2, 3, 4, 5, 6}
s1.intersection_update(s2)  # 원본값을 교집합으로 변경
print(s1)  # {5, 6}


# 대칭차, 둘 중 한 집합에만 속하는 원소들의 집합
s1 = {1, 2, 3, 4, 5, 6}
print(s1.symmetric_difference(s2))  # 대칭차 리턴, {1, 2, 3, 4, 7, 8, 9}

print(s1)  # {1, 2, 3, 4, 5, 6}
s1.symmetric_difference_update(s2)  # 원본값을 대칭차로 변경
print(s1)  # {1, 2, 3, 4, 7, 8, 9}
