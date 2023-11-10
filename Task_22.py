# Task #2
def find_max_length(tree):
    dct = {}
    for edge in tree:
        a, b = edge
        if a not in dct:
            dct[a] = []
        if b not in dct:
            dct[b] = []
        dct[a].append(b)
        dct[b].append(a)

    def dfs(node, visited):
        visited.add(node)
        max_length = 0
        for neighbor in dct[node]:
            if neighbor not in visited:
                path_length = 1 + dfs(neighbor, visited)
                max_length = max(max_length, path_length)
        return max_length

    max_path_length = dfs(1, set())

    return max_path_length

tree = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]
result = find_max_length(tree)
print(result)

# Task #3

import keyword

def replace_keywords(text):
    keywords_set = set(keyword.kwlist)
    words = text.split()
    modified_text = ' '.join('<kw>' if word in keywords_set else word for word in words)
    return modified_text

input_text = "if x and y or not z"
result = replace_keywords(input_text)
print(result)