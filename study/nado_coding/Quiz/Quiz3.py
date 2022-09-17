# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예)http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

# 생성된 비밀번호: nav51!

domain = "http://naver.com"
domain = domain[7:]
domain = domain[:-4]
pw = domain[:3] + str(len(domain)) + str(domain.count("e")) + "!"
print(pw)

url = "http://naver.com"
my_str = url.replace("http://", "") 
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다." .format(url, password))