# Task #1
def extr_x(dct, x):
    res = []
    for k, v in dct.items():
        if k == x:
            res.append(v)
        if isinstance(v, dict):
            res.extend(extr_x(v, x))
    return res
dct = {1: 1, 2: 2, 3: {2: 22, 3: {1: 111, 2: 222, 3: {0: 1111, 1: 2222, 2: 3333}}, 1: 11}, 6: 22}
x = 1
res = extr_x(dct, x)
print(res)


# Task #2
import re
def car_numbers(nums):
    regex = r'([A-Za-z]{1}\d{3}[A-Za-z]{2}(78|178))'
    car_numbers = re.findall(regex, nums)
    for match in car_numbers:
        number = match[0]
        if number.endswith('78'):
            formatted_number = f"{number[:1]}{number[1:4]}{number[4:6]}{number[6:8]}"
        else:
            formatted_number = f"{number[:1]}{number[1:4]}{number[4:6]}{number[6:9]}{number[9:11]}"
        print(formatted_number)
nums = "номера автомобилей: A123BC78, X666XX178, но не Z99ZZ99."
car_numbers(nums)


# Task #3
import re
def phone_numbers(nums):
    regex = r'(\+7\((812|921)\)\d{3}-\d{2}-\d{2}|\+7\((812|921)\)\d{7})'
    phone_numbers = re.findall(regex, nums)
    for match in phone_numbers:
        number = match[0]
        print(number)
nums = "Текст с номерами: +7(812)123-45-67, +7(921)9876543, но не +7(123)123-4567."
phone_numbers(nums)