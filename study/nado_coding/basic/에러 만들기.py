# 사용자 정의 에러 만들기
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        #raise ValueError # 의도적으로 오류 발생, 파이썬 내장 오류
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 사용자가 정의한 에러
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력했습니다. 한 자리 숫자만 입력하세요.")
except  BigNumberError as err:
    print("에러가 발생했습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.") # 실행되든, 오류가 발생하든 무조건 실행됨