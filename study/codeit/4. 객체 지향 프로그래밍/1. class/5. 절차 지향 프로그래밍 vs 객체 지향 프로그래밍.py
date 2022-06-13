# 두 프로그래밍의 차이점
# 절차 지향 프로그래밍
# - 프로그램을 만들 때, 데이터와 함수를 합칠 수 없다.
# - 프로그램을 명령어들을 순서대로 실행하는 것으로 본다.

# 객체 지향 프로그래밍
# - 프로그램을 만들 때, 데이터와 함수를 합칠 수 있다.
# - 프로그램을 객체들이 순서대로 소통하는 과정으로 본다.


# 절차 지향 프로그래밍
# 반복적으로 사용하는 코드를 함수로 정의한다
def print_person_info(person_name, person_age, person_gender):
    # 사람의 이름, 나이, 성별을 파라미터로 받으면 받은 정보를 이해할 수 있는 문자열로 출력해주는 함수
    print("사람 한 명을 소개합니다")
    print("{}님은 {}살이고 {}입니다".format(person_name, person_age, person_gender))


def is_underage(person_age):
    # 사람의 나이를 파라미터로 받아서 미성년자인지를 리턴해주는 함수
    return person_age < 20


# 영훈이의 정보
young_name = "영훈"
young_age = 10
young_gender = "남자"

# 윤수의 정보
yoonsoo_name = "윤수"
yoonsoo_age = 20
yoonsoo_gender = "남자"

# 영훈/윤수 정보 출력
print_person_info(young_name, young_age, young_gender)
print_person_info(yoonsoo_name, yoonsoo_age, yoonsoo_gender)

# 영훈/윤수가 미성년자인지 출력
print(is_underage(young_age))
print(is_underage(yoonsoo_age))


# 객체 지향 프로그래밍
# 속성과 행동을 갖는 객체들이 행동을 하는 방식으로 작성한다
class Person:
    # 사람을 나타내는 클래스
    def __init__(self, name, age, gender):
        # 사람은 이름, 나이, 성별을 속성으로 갖는다
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):
        # 자신의 정보를 출력하는 메소드
        print("사람 한 명을 소개합니다")
        print("{}님은 {}살이고 {}입니다".format(self.name, self.age, self.gender))

    def is_underage(self):
        # 사람의 나이를 파라미터로 받아서 미성년자인지를 리턴해주는 메소드
        return self.age < 20


# 영훈/윤수을 나타내는 객체 생성
young = Person("영훈", 10, "남자")
yoonsoo = Person("윤수", 20, "남자")

# 영훈/윤수 정보 출력
young.print_info()
yoonsoo.print_info()