# 081 * expression
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, _, __ = scores
# print(valid_score, _, __)

# 082 
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, b, *vaild_score = scores
# print(vaild_score)

# 083 
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, *vaild_score, b = scores
# print(vaild_score)

# 084 dictionary
# temp = dict()
# temp2 = {}
# print(temp, type(temp))
# print(temp2, type(temp2))

# 085
# ice_cream = {"메로나" : 1000, "폴라포" : 1200, "빵빠레" : 1800}
# print(ice_cream)

# 086 
# ice_cream["죠스바"] = 1200
# ice_cream["월드콘"] = 1500
# print(ice_cream)

# 087
# a = list(ice_cream.keys())
# print(a[0],":",ice_cream[a[0]])

# 088 값 바꾸기
# ice_cream["메로나"] = 1300
# print(ice_cream.items())

# 089 삭제
# del ice_cream["메로나"]
# print(ice_cream)

# 090 
# 없는 값을 get으로 찾으면 None이나 입력한 기본값으로
# dic[]으로 출력하면 오류가 생긴다.

# 091
# inventory = {"메로나":[300, 20], "비비빅":[400, 3], "죠스바":[250, 100]}
# print(inventory)

# 092
# print(inventory["메로나"][0], "원")

# 093
# print(inventory["메로나"][1], "개")

# 094
# inventory["월드콘"] = [500, 7]
# print(inventory)

# 095
# icecream = list(inventory.keys())
# print(icecream)

# 096
# price = list(inventory.values())
# print(price)

# 097
# print(ice_cream.values(), sum(ice_cream.values()))

# 098 딕셔너리 간의 통합
# ice = {'탱크보이':1200, '폴라포':1200, '빵빠레':1800,
#  '월드콘':1500, '메로나':1000}
# new_ice = {'팥빙수':2700, '아맛나':1000}

# ice.update(new_ice)
# print(ice)

# 099 zip & dict
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = dict(zip(keys, vals))
print(result)

# 100
data = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(data, close_price))
print(close_table)