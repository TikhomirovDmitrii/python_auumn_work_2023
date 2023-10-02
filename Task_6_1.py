# Task #1
num_arab = [1000,500,100,50,10,5,1]
num_rom = ["M","D","C","L","X","V","I"]

def roman_to_arabic():
    arabic = 0
    roman = input("Введите Римское число: ")
    for i in range(len(roman)):
        letter = roman[i]
        for j in range(len(num_rom)):
            if letter == num_rom[j]:
                arabic += num_arab[j]
    for i in range(1, len(roman)):
        letter = roman[i]
        if (letter == "M" or letter == "D") and roman[i-1] == "C":
            arabic -= 200
        elif (letter == "C" or letter == "L") and roman[i-1] == "X":
            arabic -=20
        elif (letter == "X" or letter == "V") and roman[i-1] == "I":
            arabic -= 2

    print('Арабское число: ', arabic)

# Task #3
roman_to_arabic()
s = input()
lst1 = []
lst2 = []
lst3 = []
for i in s:
    if i.isnumeric():
        lst1.append(i)
    elif i.isascii():
        lst2.append(i)
    elif i.punctuation():
        # не сообразил как вынести отдельно символы пунктуации
        lst3.append(i)

print(lst1, lst2, lst3)