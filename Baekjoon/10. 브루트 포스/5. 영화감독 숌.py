"""1436 영화감독 숌"""

# n번째 영화
n = int(input())

# 시리즈를 셀 변수
cnt = 0

# 초기 영화 이름
movie_number = 666

while True:
    # 영화 시리즈를 문자로 바꾼다
    if "666" in str(movie_number):
        cnt += 1

    # 만약 시리즈 순서와 입력받은 숫자가 같으면 출력
    if n == cnt:
        print(movie_number)
        break

    # 맞는 숫자가 아니면 다음 숫자로 넘어간다
    movie_number += 1
