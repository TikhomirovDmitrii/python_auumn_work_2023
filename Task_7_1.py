# Task #1
a = list(map(int,input('--> ').strip().split()))
x = a[0]
while 1:
    sum = 0
    for i in a:
        if x%i == 0:
            sum += 1
    if sum == len(a):
        break
    else :
        x += 1
print(x)

    # Task #2
def encypt(string, n):
    result = ""
    for i in range(len(string)):
        char = string[i]
        if (char.isupper()):
            result += chr((ord(char) + n - 64) % 26 + 65)
        else:
            result += chr((ord(char) + n - 96) % 26 + 97)
    return result
string = input('>')
n = 2

print("Input : " + string)
print("Step : " + str(n))
print("Output: " + encypt(string, n))