"""
# Composition
- 다른 클래스의 일부 메서드를 사용하고 싶지만, 상속은 하고 싶지 않은 경우

1. 부모 클래스가 변하면 자식 클래스는 계속 수정되어야 한다.
2. 부모 클래스의 메서드를 오버라이딩 하는 경우 내부 구현 방식의 얕은 이해로 오류가 생길 가능성 증가
"""


class Robot:
    population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__secret = "I am a robot"  # __ 두 개를 붙이면 private 변수
        self.__age = age
        Robot.population += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}")

    def cal_add(self, a, b):
        return a + b

    @property
    def name(self):
        """
        name Getter
        """
        return f"Hi, my name is {self.__name}."

    @property
    def age(self):
        """
        age Getter
        """
        return self.__age

    @age.setter
    def age(self, value):
        """
        age Setter
        """
        if value < 0:
            print("Age can't be negative")
        else:
            self.__age = value

    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots.")


class Cal:
    def __init__(self, name, age):
        self.Robot = Robot(name, age)

    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b)
