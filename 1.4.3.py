"""Сформувати функцію для переведення натурального числа з десяткової системи
числення у шістнадцятирічну."""
import timeit

def conversion(number): #Переведення натурального числа за допомогою рекурсії
    number, symbols = number // 16, all_symbols[number % 16]
    if number:
        return conversion(number) + symbols
    return symbols


def conversion_iter(number):  #Переведення натурального числа за допомогою ітерації
    result = ""
    if number == 0:
        return 0
    while number != 0:
        symbols = number % 16
        number = number // 16
        result += all_symbols[symbols]
    return result[::-1]


all_symbols = "0123456789ABCDEF" #Усі символи шістнадцятирічної системи числення

number = int(input('Введіть число: '))
print(number)
check = int(input('Виберіть тип виконання операції: 1 - рекурсія, 2 - ітерація. '))
if check == 1:
    print(conversion(number))  # Вибір виконання
elif check == 2:
    print(conversion_iter(number))

t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)  # Обрахування часу виконання програми
print(f"Програма виконана за {t} секунд")