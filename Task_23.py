# Task #1
import psycopg2
def longest_palindrome(s):
    n = len(s)
    if n <= 1:
        return n

    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    start = 0
    max_length = 1

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if dp[i + 1][j - 1] and s[i] == s[j]:
                dp[i][j] = True
                start = i
                max_length = k

    return max_length, s[start:start + max_length]

input_str = "aabbcczddzcc"
length, substring = longest_palindrome(input_str)
print(f"Длина наибольшей палиндромной подстроки: {length}")
print(f"Наибольшая палиндромная подстрока: {substring}")

# Task #2
import psycopg2
import pandas as pd
con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="",
    host="127.0.0.1",
    port="5432"
)

cur = con.cursor()
cur.execute("SELECT * FROM BOOK2")

rows = cur.fetchall()
df = pd.DataFrame(rows)

for row in rows:
    print(df)

# Task #3
from functools import cmp_to_key

def largest_number(nums):
    nums_str = [str(num) for num in nums]

    def compare(x, y):
        return int(x + y) - int(y + x)

    nums_str_sorted = sorted(nums_str, key=cmp_to_key(compare), reverse=True)
    result = ''.join(nums_str_sorted)

    return result

input_nums1 = [1, 21, 3]
result1 = largest_number(input_nums1)
print(result1)

input_nums2 = [9, 81, 25]
result2 = largest_number(input_nums2)
print(result2)
