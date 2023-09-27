def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1/num2

def multi(num1,num2):
    return num1*num2

def main():
    operation = input("What do you want to do?(+, -, *, or /):")
    if (operation != "+" and operation != "-" and operation != "*" and operation != "/"):
        print("Your input is invalid. Please enter a valid input.")
    else:
        num1 = float(input("Enter value for num1: "))
        num2 = float(input("Enter value for num2: "))
        if (operation == "+"):
            print(add(num1, num2))
        elif (operation == "-"):
            print(subtract(num1, num2))
        elif (operation == "*"):
            print(multi(num1,num2))
        elif (operation == "/"):
            print(div(num1,num2))

if name == 'main':
    while(True):
        main()
        if input('If you are done with calculating, type q: ') == 'q':
           break

s1, s2 = input("> "), input("> ")
rip1 = s1.strip('1234567890 !?:"<>,.')
rip2 = s2.strip('1234567890 !?:"<>,.')
dct1, dct2 = {}, {}
for i in rip1:
    dct1[i] = dct1.get(i, 0) + 1
for i in rip2:
    dct2[i] = dct2.get(i, 0) + 1
if dct1 == dct2:
    print(True)
else:
    print(False)