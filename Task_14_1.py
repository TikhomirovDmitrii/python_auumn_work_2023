# Task #1
def count(n):
    if n < 10:
        return 1
    else:
        return 1 + count(n // 10)

n = int(input('enter_num: '))

print('num_dig:', count(n))

# Task #2
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return sum_of_digits(n // 10) + n % 10

n = int(input("--->: "))

print('Sum', n, '=', sum_of_digits(n))