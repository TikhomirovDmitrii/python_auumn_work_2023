# Task #1
from itertools import combinations, product
lst = [50, 100, 200, 500, 1000, 5000]
max_count = 1
max_sum = max_count * max(lst)
possible_sums = set()
for counts in product(range(max_count + 1), repeat=len(lst)):
    current_sum = sum(count * denom for count, denom in zip(counts, lst))
    if current_sum <= max_sum:
        possible_sums.add(current_sum)
print(sorted(possible_sums))

# Task #2
class Fibonacci:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def iter(self):
        return self

    def __next__(self):
        result = self.curr
        self.curr, self.prev = self.curr + self.prev, self.curr
        return result

fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

# Task #3
class Person:
    def __init__(self, last_name, first_name, patronymic):
        self.full_name = f"{last_name}{first_name}{patronymic}"

    def __str__(self):
        inverted_name = self.full_name[::-1]
        return inverted_name
p = Person('Иванов', 'Михаил', 'Федорович')
print(p)