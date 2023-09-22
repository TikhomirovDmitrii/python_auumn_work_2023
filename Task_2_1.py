# Task 1
n = int(input())
for i in range(10):
     print(i, "*", n,"=", i*n)

# Task 2
l = [6, 8, 2, 3, 4, 5]
min1 = l[0]
for i in range(len(l)):
    if l[i] < min1:
        min1 = l[i]
print(min1)

# Task 3
n = int(input())
factorial = n
for i in range(1, n):
    factorial = factorial * i
print(factorial)


