# Task #1
from collections import Counter

def find_single_number(nums):
    count = Counter(nums)
    for num, occurrences in count.items():
        if occurrences == 1:
            return num

numbers = [1, 1, 1, 2, 1, 1]
single_number = find_single_number(numbers)
print(single_number)

# Task #2
from collections import deque

def optimal_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and matrix[x][y] >= 0

    queue = deque([(start, 0)])
    visited = set()

    while queue:
        (x, y), current_sum = queue.popleft()

        if (x, y) == end:
            return current_sum

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            new_sum = current_sum + matrix[new_x][new_y] if is_valid(new_x, new_y) else float('-inf')

            if (new_x, new_y) not in visited and new_sum != float('-inf'):
                visited.add((new_x, new_y))
                queue.append(((new_x, new_y), new_sum))

    return None

matrix = [
    [1, 2, 3],
    [4, -1, 6],
    [7, 8, 9]
]

start_point = (0, 0)
end_point = (2, 2)

result = optimal_path(matrix, start_point, end_point)
print(result)

# Task #3
def are_isomorphic(word1, word2):
    if len(word1) != len(word2):
        return False

    mapping = {}
    used = set()

    for i in range(len(word1)):
        char1, char2 = word1[i], word2[i]

        if char1 in mapping:
            if mapping[char1] != char2:
                return False
        else:
            if char2 in used:
                return False
            mapping[char1] = char2
            used.add(char2)

    return True

print(are_isomorphic("CBAABC", "DEFFED"))
print(are_isomorphic("XXX", "YYY"))
print(are_isomorphic("RAMBUNCTIOUSLY", "THERMODYNAMICS"))
print(are_isomorphic("AB", "CC"))
print(are_isomorphic("XXY", "XYY"))