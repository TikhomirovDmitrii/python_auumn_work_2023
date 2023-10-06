Task #1
x = input("> ").replace('AG', 'GA')
a = x.replace('CT', 'CAGT')
print(x)
print(a)

# Task #2
x = [[1,5,3], [2,44,1, 4], [3,3]]
x.sort(key=len)
print(x)
print(sorted(x, key = lambda l: l[-1])) #пытался сортировать подсписок, но не сработало.

Task #3
s = ['abab', 'xx', 'aaaaaaa', 'abcbab']
s.sort(key = lambda x: len(set(list(x))), reverse=True)
print(s)
