def find_optimal_route_with_path(matrix):
    if not matrix:
        return 0, []

    rows, cols = len(matrix), len(matrix[0])

    dp = [[0] * cols for _ in range(rows)]
    path = [[[] for _ in range(cols)] for _ in range(rows)]

    dp[0][0] = matrix[0][0]
    path[0][0] = [(0, 0)]

    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
        path[i][0] = path[i-1][0] + [(i, 0)]
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
        path[0][j] = path[0][j-1] + [(0, j)]

    for i in range(1, rows):
        for j in range(1, cols):
            if dp[i-1][j] < dp[i][j-1]:
                dp[i][j] = matrix[i][j] + dp[i-1][j]
                path[i][j] = path[i-1][j] + [(i, j)]
            else:
                dp[i][j] = matrix[i][j] + dp[i][j-1]
                path[i][j] = path[i][j-1] + [(i, j)]

    return dp[rows-1][cols-1], path[rows-1][cols-1]

matrix = [
    [10, 20, 30],
    [5, 1, 80],
    [90, 2, 70]
]

result, optimal_path = find_optimal_route_with_path(matrix)
print("Оптимальная сумма:", result)
print("Оптимальный путь:", optimal_path)