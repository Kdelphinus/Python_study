# 코로나로 인해 영화관의 자리는 홀수번만 예약할 수 있도록 바꿔야 한다.

# 조건
# 각 열은 1 ~ 20번까지 총 20개의 좌석으로 구성되며 A 열에 대해서만 출력한다. 

# 출력결과
# A1 A3 A5 A7 A9 A11 A13 A15 A17 A19

# movie_seat = range(1, 21)
# for i in movie_seat:
#     if i % 2 == 1:
#         print("A{}".format(i), end = " ")

for i in range(1,21)[::2]:
    print("A"+str(i), end = " ")