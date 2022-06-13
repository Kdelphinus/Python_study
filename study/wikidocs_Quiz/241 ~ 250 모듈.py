# 시간
from datetime import *

# now = datetime.now()
# print(now, type(now))

# for i in range(5):
#     if i == 0:
#         print("현재시간: ", now)
#     else:
#         print("오늘로부터", i, "일 전:", now - timedelta(i))

# print(now.strftime("%H:%M:%S"))
# now_time = "2020-05-04"
# print(datetime.strptime(now_time,"%Y-%m-%d"))

from time import *
# 1초에 한 번씩 시간을 나타내는 코드
# while True:
#     now = datetime.now()
#     print(now)
#     sleep(1)

from os import *
ret = getcwd()
print(ret, type(ret))

from numpy import *
for i in arange(0, 5, 0.1):
    print(i)