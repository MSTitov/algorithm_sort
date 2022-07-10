#!/usr/bin/python3

# сортировка пузырком
def bubbleSorting() -> None:
    a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
    n = len(a)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
                a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами 

    print('сортировка пузырком:', a)

# сортировка выбором
def sortingByChoice() -> None:
    a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
    n = len(a)
    # реализация алгоритма сортировки выбором
    i = 0
    while i < n - 1:
        m = i
        j = i + 1
        while j < n:
            if a[j] < a[m]:
                m = j
            j += 1
        a[i], a[m] = a[m], a[i]
        i += 1
    print('сортировка выбором:', a)

# сортировка простыми вставками
def sortingBySimpleInserts() -> None:
    a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
    n = len(a)
    for i in range(1, n):
        elem = a.pop(i)  # первый элемент из неотсортированной части списка
        lower_bound = 0  # нижняя граница поиска
        upper_bound = i # верхняя граница поиска 
        center = lower_bound + (upper_bound - lower_bound) // 2  # центр поиска в неотсортированной части
        while lower_bound < upper_bound:
            center = lower_bound + (upper_bound - lower_bound) // 2  # центр поиска в неотсортированной части
            if elem < a[center]:
                upper_bound = center
            else:
                lower_bound = center + 1
        a.insert(lower_bound, elem)


    print('сортировка простыми вставками:', a)

def main():
    bubbleSorting()
    sortingByChoice()
    sortingBySimpleInserts()
    
if __name__ == '__main__':
    main()
