# Task #1
def count_inversions(lst):
    count = 0
    n = len(lst)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                count += 1

    return count

print(count_inversions([1, 2, 3, 4, 5]))
print(count_inversions([5, 4, 3, 2, 1]))

# Task #2
def ham(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Строки должны быть одинаковой длины")

    distance = sum(c1 != c2 for c1, c2 in zip(str1, str2))
    return distance

print(ham("abc", "abc"))
print(ham("abc", "abd"))
print(ham("abc", "xyz"))