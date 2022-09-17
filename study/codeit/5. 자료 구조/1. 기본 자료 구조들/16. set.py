finished_classes = set()

# 데이터 저장
finished_classes.add("자료 구조")
finished_classes.add("알고리즘")
finished_classes.add("프로그래밍 기초")
finished_classes.add("인터렉티브 웹")
finished_classes.add("데이터 사이언스")

print(finished_classes)

# 중복 데이터 저장 시도
finished_classes.add("자료 구조")  # set 데이터 값은 변화가 없다
finished_classes.add("알고리즘")

print(finished_classes)

# 데이터 탐색
print("컴퓨터 개론" in finished_classes)
print("자료 구조" in finished_classes)

# 데이터 삭제
finished_classes.remove("자료 구조")
finished_classes.remove("알고리즘")

print(finished_classes)

# key만 저장된 해시 테이블이기에 value를 가져올 수 없음
print(finished_classes[0])  # 오류 발생