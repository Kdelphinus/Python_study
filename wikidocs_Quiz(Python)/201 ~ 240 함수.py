# 201 ~ 203 
# def print_coin():
#     print("비트코인")

# for i in range(100):
#     print_coin()

# 204
# def print_coins():
#     for i in range(100):
#         print("비트코인")

# 206
# def message():
#     print("A")
#     print("B")

# message()
# print("C")
# message()

# 211
# def 함수(문자열):
#     print(문자열)

# 함수("안녕")
# 함수("Hi") 

# 212
# def plus(a, b):
#     print(a+b)
# plus(3, 4)
# plus(7, 8)

215, 216
# def print_with_smile():
#     print(input("문자를 입력하세요.")+":D")

# print_with_smile()

# def print_with_smile(string):
#     print(string + ":D")
# print_with_smile("안녕하세요.")

217
# def print_upper_price(price):
#     print(price * 1.3)
# print_upper_price(1000)

218
# def print_sum(a, b):
#     print(a+b)

219
# def print_arithmetic_operation(a, b):
#     print("{0} + {1} = {2}".format(a, b, a + b))
#     print("{0} - {1} = {2}".format(a, b, a - b))
#     print("{0} * {1} = {2}".format(a, b, a * b))
#     print("{0} / {1} = {2}".format(a, b, a / b))
# print_arithmetic_operation(3, 4)

220
# def print_max(a, b, c):
#     if a > b and a > c:
#         print("max:", a)
#     elif b > a and b > c:
#         print("max:", b)
#     elif c > a and c > b:
#         print("max:", c)
#     elif a == b and a != c:
#         print("max(a=b):", a)
#     elif a == c and a != b:
#         print("max(a=c):", a)
#     elif c == b and a != c:
#         print("max(b=c):", b)
#     else:
#         print("max(a=b=c):", a)
# print_max(5,5,5)

221
# def print_reverse(string):
#     print(string[::-1])
# print_reverse("pt")

222
# def print_socre(score_list):
#     print(sum(score_list)/len(score_list))
# print_socre([5,5,3,6,7,5])

223
# def print_even(num_list):
#     for i in num_list:
#         if i % 2 == 0:
#             print(i)
# print_even([5,2,3,6,8,7,4])

224
# def print_keys(dic):
#     for key in dic.keys():
#         print(key)
# print_keys({"이름":"홍길동", "나이":34, "성별":"남"})

225
# def print_value_by_key(dict, date):
#     print(dict[date])
# my_dict = {"10/26":[100, 130, 100, 100], "10/27":[10, 12, 10, 11]}

# print_value_by_key(my_dict, "10/27")

226
# def print_mxn(line):
#     chunk_num = int(len(line)/5)
#     for x in range(chunk_num + 1):
#         print(line[x * 5:x * 5 + 5])
# print_mxn("가나다라마바사아자차카타파하")

227
# def print_mxn(line, a):
#     chunk_num = int(len(line)/a)
#     for x in range(chunk_num + 1):
#         print(line[x * a:x * a + a])
# print_mxn("가나다라마바사아자차카타파하",3)

# 228 return 함수에 대해서
# def calc_monthly_salary(annual_salary):
#     print(int(annual_salary/12))
# a = calc_monthly_salary(115324786221)
# print(a)

# def calc_monthly_salary(annual_salary):
#     monthly_pay = int(annual_salary / 12)
#     return monthly_pay  
# a = calc_monthly_salary(115324786221) # return 함수를 넣으면 a의 값이 저장
# print(a)

# 229, 230
# def my_print(a, b):
#     print("왼쪽:", a)
#     print("오른쪽:", b)
# my_print(a=100, b=200) # 오류가 나지 않고 my_print(100, 200)과 동일하게 출력
# my_print(b=100, a=200) # my_print(200, 100)과 동일하게 출력

# 232
# def make_url(string):
#     url = "www." + string + ".com"
#     return url

#     # return "www." + string + ".com" 도 같은 결과

# 233
# def make_list(string):
#     my_list=[]
#     for i in string:
#         my_list.append(i)
#     return my_list

# def make_list2(string):
#     return list(string)

# a = make_list2('abck')
# print(a)

# 234
# def pickup_even(my_list):
#     a_list = []
#     for i in my_list:
#         if i % 2 == 0:
#             a_list.append(i)
#     return a_list
# b = pickup_even([5,1,2,3,8,9,7])
# print(b)

# 235
# def convert_int(string):
#     return int(string.replace(",", ""))
# a = convert_int("4523,3245,66")
# print(a)