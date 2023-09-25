# Task #1
i = []
while True:
    n = int(input())
    if n==0:
        break
    i.append(n)
avr = sum(i)/len(i)
print(avr)

# Task #2
n = "133244459"
a = list(n)
b = []
for x in range (0,len(a)):
    y=0
    i=0
    count=0
    if a[x] not in b:
        b.append(a[x])
        while i < len(a) :
            if a[x] == a[i]:
                count = count+1
            i = i+1
        print(a[x],count)

# Task #3
s = "I found an epic new UK tabletop game"
b = max(s.split(), key=len)
print(b)