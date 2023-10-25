# Task #1
import re
def fn(s):
    words = re.findall(r'\b\w', s)
    acronym = ''.join(word.upper() for word in words)
    return acronym
s = "Институт точной механики оптики"
acronym = fn(s)
print(acronym)



# Task #2
import re
def fn(x, s):
    pattern = r'\b(?:[0-9]|1[0-5])\b'
    nums = re.findall(pattern, s)
    return [int(num) for num in nums]

# Пример использования:
x = 16
s = "0 1 12 45 46 100 1000"
result = fn(x, s)
print(result)

# Task #3
def lowercase_deco(func):
    def wrapper():
        or_res = func()
        modi = or_res.lower()
        return modi
    return wrapper
# @lowercase_deco
def h():
    return 'Hello'
h = lowercase_deco(h)
print(h())