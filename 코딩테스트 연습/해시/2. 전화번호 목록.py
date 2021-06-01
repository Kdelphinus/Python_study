"""나의 풀이"""


def solution(phone_book):
    # 문자 안 숫자를 기준으로 정렬
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        # phone_book[j]의 시작이 phone_book[i]인지 확인하는 함수
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True


a = ["1123", "25", "96", "112345689875", "112"]
a.sort()
print(a)

print(solution(a))


"""모범 답안"""