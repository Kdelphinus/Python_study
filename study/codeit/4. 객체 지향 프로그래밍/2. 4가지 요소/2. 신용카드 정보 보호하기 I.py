class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        self.__name = name
        self.__password = password
        self.__payment_limit = payment_limit

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_password(self):
        return "비밀 번호는 볼 수 없습니다"

    def set_password(self, value):
        self.__password = value

    def get_payment_limit(self):
        return self.__payment_limit

    def set_payment_limit(self, value):
        if value >= 0 and value <= CreditCard.MAX_PAYMENT_LIMIT:
            self.__payment_limit = value
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")


card = CreditCard("강영훈", "123", 100000)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())

card.set_name("성태호")
card.set_password("1234")
card.set_payment_limit(-10)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())