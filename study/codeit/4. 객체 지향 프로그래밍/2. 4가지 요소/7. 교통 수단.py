from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        """ 교통 수단의 주행을 시작한다 """
        pass

    @property
    @abstractmethod
    def speed(self):
        """ _speed에 대한 추상 getter 메소드 """
        pass

    def stop(self):
        """ 교통 수단의 속도를 0으로 바꾼다 """
        self.speed = 0  # 앞으로 정의될 setter 함수 speed를 실행하는 방향


print(Vehicle.mro())
print(dir(Vehicle))