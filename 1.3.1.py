"""1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n."""
import timeit



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_iter(n):
    if n == 0 or n == 1:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res


check = int(input('Виберіть тип обчислення факторіалу: 1 - рекурсія, 2 - ітерація. '))
if check == 1:
    print(factorial(int(input('Введіть число: ')))) #Вибір виконання
elif check == 2:
    print(factorial_iter(int(input('Введіть число: '))))



t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000) #Обрахування часу виконання програми
print(f"Програма виконана за {t} секунд")