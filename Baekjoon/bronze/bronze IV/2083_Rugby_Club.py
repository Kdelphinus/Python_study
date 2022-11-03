while True:
    name, age, weight = input().split()
    if name == "#" and age == weight == "0":
        break
    print(name, end=" ")
    print("Senior") if int(age) > 17 or int(weight) >= 80 else print("Junior")
