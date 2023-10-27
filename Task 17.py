# Task #1
def remove_duplicate_words(text):
    words = text.split()
    lst = []

    for word in words:
        if word not in lst:
            lst.append(word)

    res = ' '.join(lst)
    return res

s = input()
result = remove_duplicate_words(s)
print(result)

# Task #2
def uppercase_args_deco(func):
    def wrapper(*args, **kwargs):
        args = [arg.upper() if isinstance(arg, str) else arg for arg in args]
        return func(*args, **kwargs)
    return wrapper

@uppercase_args_deco
def fn(arg1, arg2, arg3="default"):
    print(arg1, arg2, arg3)
fn("Hello", 123, arg3="World")

# Task #3
# class Shape:
#     def init(self, colour, square):
#         self.colour = colour
#         self.square = square
#
#     def set_colour(self, colour):
#         self.colour = colour
#
#     def get_colour(self):
#         return self.colour
#
#     def set_square(self, square):
#         self.square = square
#
#     def get_square(self):
#         return self.square
#
# a = Shape("Red", 5.0)  не принял аргументы
# a.set_colour("Blue")#
# print(f"Color:", a.get_colour())#
# a.set_square(75.0)
# print(f"Square:", a.get_square())

class Shape:
    def init(self):
        self.colour = ""
        self.square = 0.0

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_square(self, square):
        self.square = square

    def get_square(self):
        return self.square

my_shape = Shape()
my_shape.set_colour("Red")
print("Color:", my_shape.get_colour())
my_shape.set_square(69)
print("Square:", my_shape.get_square())