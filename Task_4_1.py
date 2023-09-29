s1, s2 = input("> "), input("> ")
rip1 = s1.strip('1234567890 !?:"<>,.')
rip2 = s2.strip('1234567890 !?:"<>,.')
dct1, dct2 = {}, {}
for i in rip1:
    dct1[i] = dct1.get(i, 0) + 1
for i in rip2:
    dct2[i] = dct2.get(i, 0) + 1
if dct1 == dct2:
    print(True)
else:
    print(False)