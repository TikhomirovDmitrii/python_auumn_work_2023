# Task_1
def num_gen():
    n=1
    while True:
        for n in range(1,100):
            if n%2 == 0:
                n=-n
            else: n
            yield n
gf = num_gen()
for i in range(6):
    print(next(gf), end=" ")

# Task #2
from itertools import count
def Palindrome():
    yield 0
    for num in count(1):
        i = 10 ** ((num - 1) // 2)
        for s in map(str, range(i, 10 * i)):
            yield int(s + s[-(num % 2)-1::-1])
gf = Palindrome()
for i in range(100):
    print(next(gf), end=" ")

# Task #3
def generate_odds(nums):
    for num in nums:
        if num % 2 == 1:
            yield num
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gf = generate_odds(numbers)
for i in gf:
    print(i, end=" ")