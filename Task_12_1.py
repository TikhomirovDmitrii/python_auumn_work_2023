# Task #2
a = [x for x in range(1, 11) for _ in range(x)]
print(a)

# Task #3
def s_ranges(ranges: str):
    ranges = ranges.split(',')
    result = []
    for i in ranges:
        a, b = i.split('-')
        a, b = int(a), int(b) + 1
        if a <= b:
            result += list(range(a, b))
            return result
print(s_ranges('1-2, 3-6'))