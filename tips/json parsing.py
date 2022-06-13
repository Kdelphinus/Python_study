# 출처: https://twpower.github.io/140-parsing-json-in-python

import json

with open("Python\여러 기능들\json_example.json") as json_file:
    json_data = json.load(json_file)

# 문자열
# key가 json_string인 문자열 가져오기
json_string = json_data["json_string"]
print(json_string)

# 숫자
# key가 json_number인 숫자 가져오기
json_number = json_data["json_number"]
print(str(json_number))  # 숫자이기 때문에 str()함수를 이용

# 배열
# key가 json_array인 배열 가져오기
json_array = json_data["json_array"]
print(json_array)

# 객체
# key가 json_object인 객체 가져와서 만들기
# json object의 경우에 python ojbect로 바꿀때는 따로 처리를 해줘야합니다.
# 기본형은 dictionary입니다.
json_object = json_data["json_object"]
print(json_object)

# bool형
# key가 json_bool인 bool형 자료 가져오기
json_bool = json_data["json_bool"]
print(json_bool)
