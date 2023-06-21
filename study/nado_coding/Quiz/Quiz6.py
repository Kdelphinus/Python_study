# 표준 체중을 구하는 프로그램을 작성하시오.

# (성별에 따른 공식)
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#     함수명 : std_weight
#     전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다.

# def std_weight(height, gender):
#     if gender == "남자":
#         return 22 * height * height
#     else:
#         return 21* height * height
# height = print("키를 입력하세요."), input()
# gender = print("성별을 입력하세요."), input()
# weight = std_weight(height / 100, gender)
# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다." .format(height, gender, weight))


def std_weight(height, gender):  # 키는 m 단위, 성별은 남자/여자
    if gender == "남자":
        return 22 * height * height
    else:
        return 21 * height * height


height = 175  # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm의 {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
