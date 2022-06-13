""" ternary expression """
# 일반적인 if문
condition = True
if condition:
    condition_string = "nice"
else:
    condition_string = "not nice"
print(condition_string)  # => nice

# ternary expression을 사용할 때
condition = True
condition_string = "nice" if condition else "not nice"
print(condition_string)  # => nice