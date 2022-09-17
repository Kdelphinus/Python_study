def binary_search(element, some_list):
    check = int(len(some_list) / 2)
    while True:
        if element > some_list[check] and check < len(some_list) - 1:
            check = int(check * 1.5)
        elif element < some_list[check] and check > 0:
            check = int(check * 0.5)
        elif element == some_list[check]:
            return check
            break
        elif check == 0 or check == len(some_list) - 1:
            if element == some_list[check]:
                return check
                break
            else:
                return None
                break


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))