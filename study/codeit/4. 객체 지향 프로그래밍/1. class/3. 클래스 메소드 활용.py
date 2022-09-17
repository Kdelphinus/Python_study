class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        parameter_list = string_params.split(",")
        name = parameter_list[0]
        email = parameter_list[1]
        password = parameter_list[2]

        return User(name, email, password)

    @classmethod
    def from_list(cls, list_params):
        name = list_params[0]
        email = list_params[1]
        password = list_params[2]

        return User(name, email, password)


# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)