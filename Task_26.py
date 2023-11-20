# Task #1
def compare_strings(str1, str2):
    len1, len2 = len(str1), len(str2)

    if abs(len1 - len2) > 1:
        return False

    if str1 == str2:
        return True

    diff_index = next((i for i, (c1, c2) in enumerate(zip(str1, str2)) if c1 != c2), None)

    if abs(len1 - len2) == 1:
        if len1 > len2:
            str2 = str2[:diff_index] + str2[diff_index + 1:]
        else:
            str1 = str1[:diff_index] + str1[diff_index + 1:]

    return str1 == str2

# Task #2
def dis(self):
    for key, value in self.dict.items():
        print(f"{key}: {value}")

Pet = type('Pet', (), {'dis': dis})

my_pet = Pet()
my_pet.name = 'Tom'
my_pet.age = 3

print(my_pet.dis())

# Task #3
class Person:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 1 <= value <= 100:
            self._age = value
        else:
            print("Недопустимый возраст")

    @age.deleter
    def age(self):
        print("Удаление возраста")
        del self._age

person = Person()
person.age = 25
print(person.age)  # 25
person.age = 120
del person.age