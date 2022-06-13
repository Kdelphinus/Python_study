# import theater_module 
# theater_module.price(3) # 3명이 영화보러 갔을 때 가격
# theater_module.price_morning(4) #4명이 조조 영화를 봤을 때 가격
# theater_module.price_soldiers(5) #5명의 군인이 영화보러 갔을 때

# import theater_module as mv #theater_module을 mv로 호출할 수 있도록 함
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldiers(5)

# from theater_module import * # 함수를 그냥 사용
# price(3)
# price_morning(4)
# price_soldiers(5)

# from theater_module import price, price_morning # 쓰고 싶은 함수만 명시
# price(3)
# price_morning(4)
# price_soldiers(5) # 오류가 남

from theater_module import price_soldiers as price # 군인만 있을 때 함수명을 줄이기 위해 별명을 붙임
price(5) #그렇기에 결과값은 일반 가격이 아닌 군인 할인 가격이 나옴