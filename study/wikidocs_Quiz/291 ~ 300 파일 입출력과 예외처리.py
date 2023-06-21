# 291
# 매수종목1 = open("매수종목1.txt", "w", encoding="utf8")
# print("005930", file = 매수종목1)
# print("005380", file = 매수종목1)
# print("035420", file = 매수종목1)
# 매수종목1.close()

# 292
# f = open("매수종목2.txt", "w", encoding = "utf8")
# f.write("005930  삼성전자\n")
# f.write("005380  현대차\n")
# f.write("035420  NAVER\n")
# f.cloes()

# 293 하라는대로 했으나 실행 안됨
# import csv

# f = open("매수종목.csv", mode = "wt", encoding = "cp949", newline = "")
# writer = csv.writer(f)
# writer.writerow(["종목명", "종목코드", "PER"])
# writer.writerow(["삼성전자", "005930", 15.79])
# writer.writerow(["NAVER", "035420", 55.82])
# f.cloes()

# 294
# f = open("매수종목1.txt", "r", encoding="utf8")
# lines = f.readlines()

# codes = []
# for line in lines:
#     code = line.strip() # '\n'
#     codes.append(code)

# print(codes)

# f.close()

# 295
# f = open("매수종목2.txt", "r", encoding="utf8")
# lines = f.readlines()

# codes = {}
# for line in lines:
#     line = line.strip() # '\n' 제거
#     k, v = line.split()
#     codes[k] = v

# print(codes)
# f.close()

# 296
# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except ValueError:
#         print(0)

# 297
# per = ["10.31", "", "8.00"]
# new_per = []

# for i in per:
#     try:
#         v = float(i)
#     except:
#         v = 0
#     new_per.append(v)

# print(new_per)

# 298
# try:
#     a = 8
#     b = 2
#     c = 0
#     print(a/c)
# except ZeroDivisionError as err:
#     print("0으로 숫자를 나눌 수 없습니다.")
#     print(err)

# 299
# data = [1, 2, 3]

# for i in range(5):
#     try:
#         print(data[i])
#     except IndexError as e:
#         print(e)

# 300
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("이상없음")
    finally:
        print("계산 끝")
