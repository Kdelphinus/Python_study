# 131, 132
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)
#     print("#####")

# 133, 134
# for 변수 in ["A", "B", "C"]:
#     print(변수)

# list = ["A", "B", "C"]
# print(list[0])
# print(list[1])
# print(list[2])

# 135
# for 변수 in ["A", "B", "C"]:
#     b = 변수.lower()
#     print("변환: ", b)

# print("a",  "b", "c")

# 136 137
# for 변수 in [10, 20, 30]:
#     print("변수: ", 변수)

# 138
# num = [10,20,30]
# a = "-------"
# for i in num:
#     print(i)
#     print(a)

# 139
# print("++++")
# for j in num:
#     print(j)

# 140
# for i in [1,2,3,4]:
#     print("-------")

# 141
# 리스트 = [100,200,300]
# for i in 리스트:
#     print(i+10)

# 142
# list = ["김밥", "라면", "튀김"]
# for i in list:
#     print("오늘의 메뉴:", i)

# 143
# list = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in list:
#     print(len(i))

# 144 145
# list = ["dog", "cat", "parrot"]
# for animal in list:
#     print(animal, len(animal))

# for animal in list:
#     print(animal[0])

# 146 147
# list = [1,2,3]
# for num in list:
#     print("3 x", num)

# for num in list:
#     print("3 x {0} = {1}".format(num, num * 3))

# 148 ~ 150
# list = ["가", "나", "다", "라"]
# for word in list[1:]:
#     print(word)

# print(" ")

# list2 = list[0] + list[2]
# for word in list2:
#     print(word)

# print(" ")

# for word in list[::2]:
#     print(word)

# print(" ")

# for word in list[::-1]:
#     print(word)

# 151
# list = [3, -20, -3, 44]
# for num in list:
#     if num < 0:
#         print(num)

# 152
# list = [3,100,23,44]
# for num in list:
#     if num % 3 == 0:
#         print(num)

# 153
# list = [13,21,12,14,30,18]
# for num in list:
#     if num % 3 == 0 and num < 20:
#         print(num)

# 154
# list  = ["I", "study", "python", "language", "!"]
# for word in list:
#     if len(word) >= 3:
#         print(word)

# 155, 156
# list = ["A", "b", "c", "D"]
# for word in list:
#     if word.isupper() == True:
#         print(word)

# print("-------")

# for word in list:
#     if word.islower() == True:
#         print(word)

# 157
# list = ["dog", "cat", "parrot"]
# for word in list:
#     print(word[0].upper() + word[1:])

# 158
# list = ["hello.py", "ex01.py", "intro.hwp"]
# for word in list:
#     print(word.split(".")[0])

# 159, 160
# list = ["intra.h", "intra.c", "define.h", "run.py"]
# for word in list:
#     if word.split(".")[1] == "h":
#         print(word)

# print(" ")

# for word in list:
#     if word.split(".")[1] == "h" or word.split(".")[1] == "c":
#         print(word)

# 161
# for num in range(1, 100):
#     print(num)

# 162
# for num in range(2002,2051,4):
#     print(num)

# 163
# for num in range(1, 31):
#     if num % 3 == 0:
#         print(num)

# 164
# for num in range(0,100):
#     print(99 - num)

# 165
# for num in range(0,10):
#     print(num / 10)

# 166
# for num in range(1,10):
#     print("3x{0} = {1}".format(num, num * 3))

# 167
# for num in range(1,10):
#     if num % 2 == 1:
#         print("3x{0} = {1}".format(num, num*3))

# 168
# i = 0
# for num in range(1,11):
#     i += num
# print(i)

# 169
# i = 0
# for num in range(1,11):
#     if num % 2 == 1:
#         i += num
# print(i)

# 170
# i = 1
# for num in range(1,11):
#     i *= num
# print(i)

# 171 ~ 174
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(price_list[i])

# print("")

# for i in range(len(price_list)):
#     print(i, price_list[i])

# print("")

# for i in range(len(price_list)):
#     print(len(price_list) - i - 1, price_list[i])

# print("")

# for i in range(1,4):
#     print(90 + i*10, price_list[i])

# 175
# my_list = ["가", "나", "다", "라"]
# for i in range(1, len(my_list)):
#     print(my_list[i-1], my_list[i])

# 176
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(2, len(my_list)):
#     print(my_list[i-2], my_list[i-1], my_list[i])

# 177
# my_list = ["가", "나", "다", "라"]
# my_list.reverse()
# for i in range(1, len(my_list)):
#     print(my_list[i-1], my_list[i])

# 178
# my_list = [100, 200, 400, 800]
# for i in range(1, len(my_list)):
#     print(my_list[i]-my_list[i-1])

# 179
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(1, len(my_list) - 1):
#     print((my_list[i-1] + my_list[i] + my_list[i+1]) / 3)

# 180
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility = []
# for i in range(0, len(low_prices)):
#     volatility.append(high_prices[i] - low_prices[i])
# print(volatility)

# 181
# apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]

# 182
# stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]

# 183
# stock = {"시가":[100, 200, 300], "종가":[80, 210, 330]}

# 184
# stock = {"10/10": [80, 110, 70, 90], "10/11":[210, 230, 190, 200]}

# 185 ~ 190
# apart = [["101호", "102호"], ["201호", "202호"], ["301호", "302호"]]
# for i in apart:
#     for j in i:
#         print(j)

# print(" ")

# # apart.reverse()
# # for i in apart: 
# for i in apart[::-1]:
#     for j in i:
#         print(j)

# print(" ")

# for i in apart[::-1]:
#     for j in i[::-1]:
#         print(j)

# print(" ")

# for i in apart:
#     for j in i:
#         print(j)
#         print("-----")

# print(" ")

# for i in apart:
#     for j in i:
#         print(j)
#     print("-----")

# print(" ")

# for i in apart:
#     for j in i:
#         print(j)
# print("-----")

# 191, 192
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for row in data:
#     for col in row:
#         print(col * 1.00014)
#     print("-----")

# 193, 194
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for row in data:
#     sub = []
#     for col in row:
#         sub.append(col * 1.00014)
#     result.append(sub)  
# print(result)

# 195 ~ 198
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# volatility =[]
# for i in range(1, len(ohlc)):
#     volatility.append(ohlc[i][1]-ohlc[i][2])
# print(volatility)

# 199
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for row in ohlc[1:]:
#     if row[3] > row[0]:
#         print(row[1] - row[2])

# 200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
a = 0
for i in ohlc[1:]:
    a += i[3]-i[0]
print(a)