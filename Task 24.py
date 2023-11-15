# Task #1
def custom_sort(input_list):
    n = len(input_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]

    return input_list

my_list = [64, 34, 25, 12, 22, 11, 90, 1, 111]
sorted_list = custom_sort(my_list)
print(sorted_list)


# Task #3
def is_valid_parentheses(s):
    stack = []
    parentheses_dict = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parentheses_dict.values():
            stack.append(char)
        elif char in parentheses_dict.keys():
            if not stack or parentheses_dict[char] != stack.pop():
                return False
        else:
            return False

    return not stack

# Пример использования:
print(is_valid_parentheses("()"))  # True
print(is_valid_parentheses(")(()))"))  # False
print(is_valid_parentheses("("))  # False
print(is_valid_parentheses("(()) (( () () ) () )"))  # True