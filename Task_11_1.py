# Task #1
from datetime import date, timedelta
from calendar import monthrange

def free_visit_in_year(year):
    result = []
    for month in range(1, 13):
        first_day_of_month = date(year, month, 1)
        last_day_of_month = first_day_of_month - timedelta(days=first_day_of_month.day)
        days_in_month = monthrange(year, month)[1]
        for day in range(first_day_of_month.weekday(), days_in_month + 1):
            if (day - 1) % 3 == 0:
                result.append(date(year, month, day))
    return result

free_visit = free_visit_in_year(2023)
print(f"Даты:")
for entry in free_visit:
    print(entry.strftime('%d-%m-%Y'))

# Task #3
roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
def to_roman(number):
    roman = ''
    for letter, value in roman_numbers.items():
        while number >= value:
            roman += letter
            number -= value
    return roman
num = int(input(""))

print(to_roman(num))