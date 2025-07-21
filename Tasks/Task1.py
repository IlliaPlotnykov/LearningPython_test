
# Сумма от 1 до 100
# sum=0
# i=1
# while i<=100:
#     sum+=1
#     i+=1
# print(sum)

sum=0
i=1
for i in range(1,101):
    sum+=i
    i+=1
print(sum)

numbers = list(range(5))
print(numbers)

def arithmetic(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Деление на ноль!"
    else:
        return "Неизвестная операция"

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Примеры использования:
print(is_year_leap(2020))  # Вывод: True
print(is_year_leap(2021))  # Вывод: False
print(is_year_leap(1900))  # Вывод: False
print(is_year_leap(2000))  # Вывод: True

def square(side):
    perimeter=side*4
    ploscha=side**2
    diagonal=(((side)**2)*2)**0.5
    return perimeter,ploscha,diagonal
print(square(5))

def season(number):
    if number in [1,2,12]:
        return 'zima'
    elif number in [3,4,5]:
        return 'vesna'
    elif number in [6,7,8]:
        return 'leto'
    else:
        return 'osen'
print(season(11))

def bank(a,years):
    return a*(1+years*0.1)
print(bank( a= 10, years= 5))

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
print(is_prime(73))

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def date(dd, mm, yyyy):
    if dd in range(1,29) and mm in[2] and is_year_leap(yyyy) == False:
        return True
    elif dd in range(1,30) and mm in[2] and is_year_leap(yyyy) == True:
        return True
    elif dd in range(1,31) and mm in [2,4,6,9]:
        return True
    elif dd in range(1,32) and mm in[1,3,5,7,8,10,12]:
        return True
    else:
        return False

print(date(29, 2, 2025))

def date(day, month, year):
    # Проверка корректности месяца
    if month < 1 or month > 12:
        return False

    # Количество дней в каждом месяце
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Проверка високосного года
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29

    # Проверка корректности дня
    if day < 1 or day > days_in_month[month - 1]:
        return False

    return True
