import pickle

# profile_file = open("profile.pickle", "wb") # b는 바이너리를 의미, 피클에선 b가 필수
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()


# 파일명이 pickle이면 오류
