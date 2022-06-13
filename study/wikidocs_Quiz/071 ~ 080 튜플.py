# 071
# my_variable = ()
# print(my_variable, type(my_variable))

# 072
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

# 073
test = (1,)

# 074
# t = (1,2,3)
# t[0] = 'a'
# tuple은 변경 불가로 오류

# 075
# t =1,2,3,4
# print(type(t))
# tuple은 괄호를 쓰지 않아도 지정 가능

# 076
# tuple은 값을 변경할 수 없기 때문에 변수 자체를 변경해야한다.

# 077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest_list = list(interest)
print(interest_list, type(interest_list))

# 078
interest_tuple = tuple(interest_list)
print(interest_tuple, type(interest_tuple))

# 079
temp = ('apple', 'banana', 'cake')
a,b,c = temp
print(a,b)
print(a,b,c)

# 080
even = tuple(range(2,100,2))
print(even)