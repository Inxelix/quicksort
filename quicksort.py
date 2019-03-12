from random import choice


def user_input():
    return list(map(int, input("Введите массив через пробел:\n").split()))


def separate(array):
    even_numbers = []
    odd_numbers = []

    for elem in array:
        if elem % 2 == 0:
            even_numbers.append(elem)
        else:
            odd_numbers.append(elem)

    return list(quicksort(even_numbers)) + list(reversed(quicksort(odd_numbers)))


def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = choice(array)
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array


array = separate(user_input())

print(*array)
