from math import sqrt
from abc import ABC, abstractmethod


class Shape(ABC):
    """도형 클래스"""

    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass


class Paint:
    """그림판 프로그램 클래스"""

    def __init__(self):
        self.shapes = []

    """ type hinting으로 Shape 타입을 가지는 인스턴스가 shape 파라미터로 들어와야 함을 알려줌 """

    def add_shape(self, shape: Shape):
        """도형 인스턴스만 그림판에 추가한다"""
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("도형 클래스가 아닌 인스턴스는 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])


class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

    def perimeter(self):
        return sqrt(self.base ** 2 + self.height ** 2) + self.base + self.height


# 테스트 코드
right_triangle_1 = RightTriangle(3, 4)
right_triangle_2 = RightTriangle(5, 12)
right_triangle_3 = RightTriangle(6, 8)

paint_program = Paint()

paint_program.add_shape(right_triangle_1)
paint_program.add_shape(right_triangle_2)
paint_program.add_shape(right_triangle_3)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())
