# 251 ~ 260
# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def __del__(self):
#         print("나의 죽음을 알리지 말라")

#     def who(self):
#         print("이름: {0}  나이: {1}  성별: {2}".format(areum.name, areum.age, areum.gender))

#     def setInfo(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# areum = Human("홍길동", 25, "남")
# print("이름:", areum.name, "나이:", areum.age, "성별:", areum.gender)
# areum.who() # Human.sho(areum)

# areum.setInfo("아름", 25, "여자")
# areum.who()

# del areum

# 261 ~ 270
# class Stock:
#     def __init__(self, name, code, PER, PBR, Yield):
#         self.name = name
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.Yield = Yield

#     def set_name(self, name):
#         self.name = name

#     def set_code(self, code):
#         self.code = code

#     def set_PER(self, PER):
#         self.PER = PER

#     def set_PBR(self, PBR):
#         self.PBR = PBR

#     def set_Yield(self, Yield):
#         self.Yield = Yield

#     def get_name(self):
#         return self.name

#     def get_code(self):
#         return self.code

# # a = Stock(None, None)
# # 삼성 = Stock("삼성전자", "005930")
# # # print(삼성.name, 삼성.code)

# # a.set_name("LG")
# # a.set_code("005931")
# # # print(a.name, a.code)

# # b = 삼성.get_name()
# # c = 삼성.get_code()
# # print(b, c)

# Samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# # print(삼성.PER)
# # 삼성.set_PER(12.75)
# # print(삼성.PER)
# Hyundai = Stock("현대차", "005380", 8.70, 0.35, 4.27)
# LG = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

# my_list = [Samsung, Hyundai, LG]
# for i in my_list:
#     print("종목코드:", i.code, "PER:", i.PER)

# 271 ~ 280
# import random
# class Account:
#     account_count = 0
#     i = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         self.deposit_count = 0
#         self.deposit_log = []
#         self.withdraw_log = []

#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3) # zfill은 빈자리에 0을 추가
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_number = num1 + "-" + num2 + "-" + num3

#         Account.account_count += 1

#     def get_account_num(cls):
#         print(cls.account_count)

#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount
#             print("현재 잔액:",self.balance)
#             Account.i += 1
#             if Account.i == 5:
#                 self.balance *= 1.01
#                 Account.i = 0
#                 print("이자가 1% 추가되었습니다.")
#                 print("현재 잔액:", self.balance)
#         else:
#             print("잘못된 금액입니다.")

#     def withdraw(self, amount):
#         if amount >= self.balance:
#             print("한도초과입니다.")
#         elif amount > 0:
#             self.balance -= amount
#             print("현재 잔액:", self.balance)
#         else:
#             print("잘못된 금액입니다.")

#     def display_info(self):
#         print("은행이름:", self.bank)
#         print("예금주:", self.name)
#         print("계좌번호:", self.account_number)
#         print("잔고:", self.balance)

#     def withdraw_history(self):
#         for amount in self.withdraw_log:
#             print(amount)

#     def deposit_history(self):
#         for amount in self.deposit_log:
#             print(amount)

# a = Account("김민수", 100)
# b = Account("이철수", 2500)
# c = Account("박지성", 500000000000)
# a.deposit(200)
# a.deposit(300)
# a.deposit(700)
# a.deposit_history()
# c.withdraw(500)
# c.withdraw(700)
# c.withdraw(1000)
# c.withdraw_history()
# data = []
# data.append(a)
# data.append(b)
# data.append(c)

# for i in data:
#     if i.balance >= 1000000:
#         i.display_info()

# 281 ~ 287
# class 차:
#     def __init__(self, tire, price):
#         self.tire = tire
#         self.price = price

#     def 정보(self):
#         print("바퀴수", self.tire)
#         print("가격", self.price)

# class 자동차(차):
#     def __init(self, tire, price):
#         차.__init__(self, tire, price)

# class 자전차(차):
#     def __init__(self, tire, price, 구동계):
#         차.__init__(self, tire, price)
#         self.구동계 = 구동계

#     def 정보(self):
#         super().정보()
#         print("구동계", self.구동계)

# car = 자동차(4, 7000)
# bicycle = 자전차(2, 100, "시마노")

# # print(car.tire, car.price)
# # print(bicycle.price, bicycle.구동계)
# print(car.정보())
# print(bicycle.정보())

# 288
# class 부모:
#     def 호출(self):
#         print("부모호출")

# class 자식(부모):
#     def 호출(self):
#         print("자식호출")

# 나 = 자식()
# print(나.호출())

# 289
# class 부모:
#     def __init__(self):
#         print("부모생성")

# class 자식(부모):
#     def __init__(self):
#         print("자식생성")
#         super().__init__()

# 나 = 자식()
