class Rectangle:
    """직사각형 클래스"""

    def __init__(self, width, height):
        """세로와 가로"""
        self.width = width
        self.height = height

    def area(self):
        """넓이 계산 메소드"""
        return self.width * self.height

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._height = value if value > 0 else 1


""" 잘못된 예시 """
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)

#     @property
#     def width(self):
#         """가로 변수 getter 메소드"""
#         return self._width

#     @width.setter
#     def width(self, value):
#         """가로 변수 setter 메소드"""
#         self._width = value if value > 0 else 1
#         self._height = value if value > 0 else 1

#     @property
#     def height(self):
#         """세로 변수 getter 메소드"""
#         return self._height

#     @height.setter
#     def height(self, value):
#         """세로 변수 setter 메소드"""
#         self._width = value if value > 0 else 1
#         self._height = value if value > 0 else 1

""" 직사각형을 상속받지 않는 정사각형 """


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        """ 정사각형 넓이 계산 메소드 """
        return self.side * self.side

    @property
    def side(self):
        """한 변 getter 메소드"""
        return self._side

    @side.setter
    def side(self, value):
        """한 변 setter 메소드"""
        self._side = value if value > 0 else 1


rectangle_1 = Rectangle(4, 6)
square = Square(2)

rectangle_1.width = 3
rectangle_1.height = 7

print(rectangle_1.area())  # 21, 설정한대로 잘 나옴

# rectangle_2.width = 3
# rectangle_2.height = 7

# print(rectangle_2.area())  # 49, Square에서 가로나 세로 길이를 설정할 때, 다른 길이까지 같게 설정하여 오답이 나옴

# 이때 정사각형은 직사각형의 행동규약을 지킬 수 없으므로 상속 자체를 받지 않아야 함

square.side = 10

print(square.area())