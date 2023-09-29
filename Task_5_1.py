# Task #1
n = int(input("> "))
for i in range(1, n + 1):
    a = 1
    for j in range(1, i + 1):
        print(a, end=" ")
        a = int(a * (i - j) / j)
    print(" ")

# Task #2
n=int(input())
ls=[1]
for i in range(2, n):
    if n % i == 0:
        ls.append(i)
print(ls)

# Task #3
n = int(input("> "))
f=[]
for i in range(n):
    if i==0 or i==1:
        f.append(i)
    else:
        x=f[i-2]+f[i-1]
        f.append(x)
print(*f,end=' ')