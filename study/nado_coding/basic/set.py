# 집합
# 중복이 안 되고 순서가 없음

my_set = {1, 2, 3, 3, 3}
print(my_set)  # 3은 중복이므로 한 번만 출력

java = {"유재석", "김태호", "조세호"}
python = set(["유재석", "박명수"])

# 교집합 (모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java나 python 중 하나 이상을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있으나 python을 못하는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹은 개발자
java.remove("김태호")
print(java)
