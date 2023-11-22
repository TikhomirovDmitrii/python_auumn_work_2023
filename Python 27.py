# Task #1
def generate_darts_matrix(n):
    if n < 1 or n > 18:
        print("Введите число n от 1 до 18.")
        return

    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n - i):
            matrix[i][j] = matrix[j][i] = matrix[n - i - 1][j] = matrix[j][n - i - 1] = min(i, j) + 1

    for row in matrix:
        print(*row)

n = int(input("Введите число n от 1 до 18: "))
generate_darts_matrix(n)

# Task #2
class Item:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name.capitalize()

    @property
    def total(self):
        return self._price * self._quantity

item1 = Item("laptop", 1200, 2)

print(item1.name)
print(item1.total)

# Task #3
def count_elements(lst):
    count = 0
    for element in lst:
        if isinstance(element, list):
            count += count_elements(element) + 1
        else:
            count += 1
    return count

print(count_elements([]))  # 0
print(count_elements([1, 2, 3]))  # 3
print(count_elements(["x", "y", ["z"]]))  # 4
print(count_elements([1, 2, [3, 4, [5]]]))  # 7