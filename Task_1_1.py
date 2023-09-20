
x = 13
y = 25
xy = x * y
print(f"{xy}")

a = 5
b = 9
ab = a + b
print(f'{ab}')

x = int(input())
y = int(input())
max_value = max(x + y, x - y, x * y, x / y, x // y)
print(max_value)


x = int(input())
y = int(input())
max_value = (x + y, x - y, x * y, x / y, x // y)
res_list = set(max_value)
res_list.remove(max(max_value))
print(max(res_list))

