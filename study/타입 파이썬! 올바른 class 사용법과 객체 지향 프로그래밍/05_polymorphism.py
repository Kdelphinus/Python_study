"""
Polymorphism

- 여러 형태를 가질 수 있도록 한다. 즉, 객체를 부품화 할 수 있도록 한다.
- 같은 형태의 코드가 다른 동작을 하도록 하는 것
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


class Siri(Robot):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        # print(self.__secret)  # __ 두 개가 붙으면 private 이기 때문에 접근 불가

    def say_apple(self):
        print(f"Hi, I'm Siri, {self.name}")

    def cal_add(self, a, b):
        return a + b + 10


def SiriKo(Robot):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def say_apple(self):
        print(f"안녕, 나는 시리야 {self.name}")

    def cal_add(self, a, b):
        return a + b + 15


def Bixby(Robot):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def say_samsung(self):
        print(f"Hi, I'm Bixby, {self.name}")

    def cal_add(self, a, b):
        return a + b + 20
