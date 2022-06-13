def is_palindrome(word):
    for index in range(len(word)):
        if word[index] != word[len(word) - index - 1]:
            return False
    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
print(is_palindrome("기러기"))
print(is_palindrome("고명준"))