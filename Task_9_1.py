s = "I'am so tiered this week"
s = sorted(s.lower())
sum = {}
for i in s:
    if i in sum:
        sum[i] += 1
    else:
        sum[i] = 1
print(str(sum))