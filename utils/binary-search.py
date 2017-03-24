def binary_search(array, number):
    pivot = len(array) / 2
    if (array[pivot] > number & len(array) > 1):
        return binary_search(array = array[:pivot], number = number)
    elif (array[pivot] < number & len(array) > 1):
        return binary_search(array = array[pivot:], number = number)
    elif (array[pivot] == number):
        return pivot
    else