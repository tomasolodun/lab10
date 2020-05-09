"""Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5."""
import random
import timeit


def maxindex(array, maxValue, index, maxIndex):
    if index == len(array):
        return maxIndex
    elif index < len(array):
        if array[index] > maxValue:
            maxValue = array[index]
            maxIndex = index
            return maxindex(array, maxValue, index + 1, maxIndex)
        else:
            return maxindex(array, maxValue, index + 1, maxIndex)



def maxindex_iter(array):
    m = 0
    for i in range(len(array)):
        if arr[i] > arr[m]:
            m = i
    return m


n = int(input('Введіть довжину масиву: '))
arr = [random.randint(1, 5) ** 2 for x in range(n)]
print(arr)

check = int(input('Виберіть тип виконання операції: 1 - рекурсія, 2 - ітерація. '))
if check == 1:
    print('Індексу максимального елемента масиву',maxindex(arr, 0, 0, 0,))  # Вибір виконання
elif check == 2:
    print('Індексу максимального елемента масиву',maxindex_iter(arr))

t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)  # Обрахування часу виконання програми
print(f"Програма виконана за {t} секунд")
