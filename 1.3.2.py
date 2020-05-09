"""'Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа."""
import timeit

def DigitalRoot(n):  #Обчислення цифрового кореня за допомогою рекурсії
    if len(str(n)) == 1:
        return n
    else:
        return DigitalRoot(sum([int(k) for k in str(n)]))


def DigitalRoot_iter(n):  #Обчислення цифрового кореня за допомогою ітерації
    res = str(n)
    while len(res) > 1:
        n = 0
        for i in res:
            n += int(i)
        res = str(n)
    return res

check = int(input('Виберіть тип обчислення цифрового кореню: 1 - рекурсія, 2 - ітерація. '))
if check == 1:
    print('Цифровий корінь дорівнює',DigitalRoot(n = int(input('Введіть число: ')))) #Вибір виконання
elif check == 2:
    print('Цифровий корінь дорівнює',DigitalRoot_iter(n = int(input('Введіть число: '))))

t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000) #Обрахування часу виконання програми
print(f"Програма виконана за {t} секунд")
