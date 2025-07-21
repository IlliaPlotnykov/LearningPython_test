# Функція для фільтрації парних чисел
def filter_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6]
print("Парні числа:", filter_even_numbers(numbers))  # Виведе: [2, 4, 6]


# Функція для підрахунку суми всіх чисел у списку
def sum_all(list_sum):
    total = 0
    for i in list_sum:
        total += i
    return total

print("Сума від 1 до 100:", sum_all(range(1, 101)))  # Виведе: 5050


# Виведення чисел від 1 до 20
list_pair = list(range(1, 21))
for i in list_pair:
    print(i)


# Таблиця множення для числа 5
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
