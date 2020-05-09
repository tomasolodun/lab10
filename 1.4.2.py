"""Сформувати функцію, що визначатиме чи є задане натуральне число простим.
Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого
себе)."""
import timeit


def prime(number, j):  #Перевірка чи є число простим за допомогою рекурсивної функції
    if number < 2:
        return 'Число не є простим'
    if j == number:
        return 'Число просте'
    if number % j == 0:
        return 'Число не є простим'
    return prime(number, j + 1)


def prime_iter(number): #Перевірка чи є число простим за допомогою ітераційної функції
    n = number
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return 'Число просте' if counter == 2 else 'Число не є простим'


number = int(input('Введіть число: '))
print(number)
check = int(input('Виберіть тип виконання операції: 1 - рекурсія, 2 - ітерація. '))
if check == 1:
    print(prime(number, 2))  # Вибір виконання
elif check == 2:
    print(prime_iter(number))

t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)  # Обрахування часу виконання програми
print(f"Програма виконана за {t} секунд")
