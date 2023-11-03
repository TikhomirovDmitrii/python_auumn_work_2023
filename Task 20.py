# Task #1
 class Cafe:
    def __init__(self, menu):
        self.menu = menu
        self.total_revenue = 0

    def serve_customer(self, customer):
        order = customer.make_order(self.menu)
        total_cost = sum(item[1] for item in order)
        self.total_revenue += total_cost

class Person:
    def __init__(self, name, payment_method):
        self.name = name
        self.payment_method = payment_method
        self.order = []

    def make_order(self, menu):
        drink, cake = random.choice(menu["drinks"]), random.choice(menu["cakes"])
        order = [(drink, menu["prices"][drink]), (cake, menu["prices"][cake])]
        self.order = order
        return order

    def pay_bill(self, cafe):
        total_cost = sum(item[1] for item in self.order)
        if self.payment_method == "cash":
            print(f"{self.name} оплачивает {total_cost} руб. наличными.")
        elif self.payment_method == "card":
            print(f"{self.name} оплачивает {total_cost} руб. картой.")
        cafe.serve_customer(self)
        self.order = []
import random
menu = {
    "drinks": ["кофе", "чай", "капучино"],
    "cakes": ["пирожное 1", "пирожное 2", "пирожное 3"],
    "prices": {
        "кофе": 100, "чай": 50, "капучино": 150,
        "пирожное 1": 70, "пирожное 2": 80, "пирожное 3": 90
    }
}
cafe = Cafe(menu)

customer1 = Person("Анна", "cash")
customer2 = Person("Петр", "card")

customer1.make_order(menu)
customer1.pay_bill(cafe)

customer2.make_order(menu)
customer2.pay_bill(cafe)

print(f"Прибыль кафе: {cafe.total_revenue} руб.")


# Task #2
import pandas as pd
def sum_numbers_in_dataframe(df):
    total_sum = 0
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            total_sum += df[column].sum()
    return total_sum
data = {'Number': [11, 22, 333, -4, 5], 'Text': ['A', 'B', 'C', 'D', 'E']}
df = pd.DataFrame(data)
result = sum_numbers_in_dataframe(df)
print(result)

# Task #3
class InfiniteSequence:
    def __init__(self):
        self.current_value = 1
        self.is_digit = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_digit:
            result = self.current_value
            self.current_value += 1
            self.is_digit = False
        else:
            result = chr(ord('A') + self.current_value - 1)
            self.is_digit = True
            self.current_value = 1 if self.current_value == 26 else self.current_value + 1
        return result

infinite_seq = InfiniteSequence()
for _ in range(150):
    print(next(infinite_seq), end = ' ')