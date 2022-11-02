# 051 list
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# print(movie_rank)

# 052 list
movie_rank.append("배트맨")
# print(movie_rank)

# 053 insert
movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)

# 054 remove
movie_rank.remove("럭키")
# print(movie_rank)

# 055 del
del movie_rank[2:]
# print(movie_rank)

# 056 
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 + lang2
# print(langs)

# 057 min, max
# nums = [1,2,3,4,5,6,7]
# print("max : ", max(nums))
# print("min : ", min(nums))

# 058 sum
# nums = [1,2,3,4,5]
# print(sum(nums))

# 059 len
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두"\
#     "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# 060 average
# nums = [1,2,3,4,5]
# avg = sum(nums) / len(nums)
# print(avg)

# 061 날짜를 제외하고 출력
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# price1 = price[1:]
# print(price1)

# 062 홀수만 출력
# nums = [1,2,3,4,5,6,7,8,9,10]
# odd = nums[::2]
# print(odd)

# 063 짝수만 출력
# nums = [1,2,3,4,5,6,7,8,9,10]
# even = nums[1::2]
# print(even)

# 064 reverse
# num = [1,2,3,4,5]
    # 방법 1
    # print(num[::-1])

#     # 방법 2
#     num.reverse()
#     print(num)

# 065
# interest = ["삼성전자", "LG전자", "Naver"]
# print(interest[0], interest[2])

# 066 join
# interest = ["삼성전자", "LG전자", "Naver", "SK하이닉스", "미래에셋대우"]
# print(" ".join(interest))

# # 067 join
# print("/".join(interest))

# # 068 join
# print("\n".join(interest))

# 069 split
# string = "삼성전자/LG전자/Naver"
# interest = string.split("/")
# print(interest)

# 070 sort
# data = [2,4,3,1,5,10,9]

# 방법 1
# data.sort()
# print(data)

# 방법 2
# a = sorted(data)
# print(a)