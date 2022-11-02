# list와 비슷하나 값을 바꿀 수 없고 속도가 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 불가'

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)