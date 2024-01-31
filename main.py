
import re

a = input("\n Введите числа : ")
n = int(input("Число для поиска : "))


#разбиваем по разделителю
res = (re.split(r"[,. ;:]", a))
#преобразуем в числа
numList = [int(x) if x.isdigit() else x for x in res]
#сортируем
numListSort = sorted(numList)


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # если x больше, чем элемент в середине, отбрасываем левую половину
        if arr[mid] < x:
            low = mid + 1

        # если x меньше, чем элемент в середине, отбрасываем правую половину
        elif arr[mid] > x:
            high = mid - 1

        # x = элементу в середине
        else:
            return mid

    # не нашли
    return -1


# вызываем функцию
result = binary_search(numListSort, n)

if result != -1:
    print("Искомое число найдено на позиции", str(result))
else:
    print("Искомое число не найдено")

