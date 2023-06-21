# 021 letters가 바인딩하는 문자열에서 첫 번째 문자와 세 번째 문자를 출력
# letters = "python"
# print(letters[0], letters[2])

# 022 뒤에 4자리만 출력
# license_plate = "24가 2210"
# print(license_plate[-4:])

# 023 '홀'만 출력
# string = "홀짝홀짝홀짝"
# print(string[0::2])
# 시작인덱스:끝인덱스:오프셋

# 024 문자열을 거꾸로 출력
# string = "PYTHON"
# print(string[::-1])
# 오프셋을 음수로 하면 뒤에서부터 출력

# 025 전화번호에서 -을 제거하고 출력
# phone_number = "010-1111-2222"
# phone_num = phone_number.replace("-", " ")
# print(phone_num)

# 026 025에 있는 번호를 붙여서 출력
# phone_num_2 = phone_number.replace("-","")
# print(phone_num_2)

# 027 url에 저장된 웹 페이지 주소에서 도메인을 출력
# url = "http://shaerbook.com"
# print(url[url.index(".") + 1:])

# url_split = url.split(".")
# print(url_split)
# print(url_split[-1])

# 028 코드 결과를 예상
# lang = "python"
# lang[0] = "p"
# print(lang) # -> 오류, 문자열은 임의의 수정이 불가

# 029 a를 A로 변경
# string = "abcdfe2A354A32A"
# string = string.replace("a","A")
# print(string)

# 030 코드 결과 예상
# string = "abcd"
# string.replace("b","B")
# print(string)
# abcd가 출력될 것, 문자열은 변경할 수 없는 자료형이기에 원본이 출력

# 031 코드 결과 예상
# a = "3"
# b = "4"
# print(a+b)
# 34, 문자열이므로

# 032 코드 결과 예상
# print("Hi" * 3)
# HiHiHi

# 033 -를 80번 출력
# print("-" * 80)

# 034 변수를 이용하여 python java python java python java python java를 출력
# t1 = "python"
# t2 = "java"
# print((t1+" "+t2+" ")*4)

# 035
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름: %s 나이: %d" % (name1, age1))
# print("이름: %s 나이: %d" % (name2, age2))

# 036 .format
# print("이름: {0} 나이: {1}" .format(name1, age1))
# print("이름: {0} 나이: {1}" .format(name2, age2))

# 037 f-string
# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")

# 038 컴마 제거하기
# 상장주식수 = "5,969,782,550"
# 상장 = 상장주식수.replace(",","")
# 상장주식수_int = int(상장)
# print(상장주식수_int)

# 039 2020/03만 출력
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:분기.index('(')])

# 040 좌우 공백 제거
# data = "  삼성전자   "
# print(data.strip())

# 041 대문자 변경
# ticker = "btc_krw"
# up_ticker = ticker.upper()
# print(up_ticker)

# 042 소문자 변경
# low_ticker = up_ticker.lower()
# print(low_ticker)

# 043 앞 글자만 대문자 변경
# test1 = "hello"
# test2 = test1.capitalize()
# print(test2)

# 044 endswith
# file_name = "보고서.xlsx"
# a = file_name.endswith("xlsx")
# print(a)

# 045 endswith
# file_name  = "보고서.xlsx"
# b = file_name.endswith("xlsx" or "xls") #file_name.endswith(("xlsx","xls"))
# print(b)

# 046 startswith
# file_name = "2020_보고서.xlsx"
# c = file_name.startswith("2020")
# print(c)

# 047 split
# a = "hello world"
# b = a.split(" ")
# print(b[0], b[1])

# 048 split
# ticker = "btc_krw"
# test = ticker.split("_")
# print(test[0],test[1])

# 049 split
# date = "2020-05-01"
# test = date.split("-")
# year = test[0]
# month = test[1]
# day = test[2]
# print(year,month,day)

# 050 rsplit
# data = "039490      "
# a = data.rsplit()
# print(a)
