# 하나의 디렉토리의 여러 모듈 파일을 모아 놓은 것이 패키지(여기선 travel)
# import travel.thailand #모듈이나 패키지까지 가능, class를 바로 불러올 수 없음
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # from문으로 쓰면 class까지 불러올 수 있음
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random

print(inspect.getfile(random))  # 모듈 위치 파악
print(inspect.getfile(thailand))
