# 인스턴스 메소드
# 인스턴스 변수, 클래스 변수 모두 사용 가능
# 인스턴스 변수가 필요할 때
def __str__(self):
    return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)


# 클래스 메소드
# 클래스 변수만 사용할 때 사용
@classmethod
def number_of_users(cls):
    print("총 유저 수는: {}입니다".format(cls.count))


# 정적 메소드
# 인스턴스 변수, 클래스 변수가 모두 필요하지 않을 때 사용
@staticmethod
def is_valid_email(email_address):
    return "@" in email_address
