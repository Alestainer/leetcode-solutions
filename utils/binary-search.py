class BinarySearcher:
    def binary_search(array, number):

        """Returns result of searching number in the array.
        Array must be sorted
        first return says if the number was found, the second - gives the coordinates of the number or the closest to the number"""
        pivot = len(array) / 2
        if (array[pivot] > number and len(array) > 1):
            return BinarySearcher.binary_search(array=array[:pivot], number=number)[0], \
                   BinarySearcher.binary_search(array=array[:pivot], number=number)[1]
        elif (array[pivot] < number and len(array) > 1):
            return BinarySearcher.binary_search(array=array[pivot:], number=number)[0], \
                   BinarySearcher.binary_search(array=array[pivot:], number=number)[1] + pivot
        elif (array[pivot] == number):
            return True, pivot
        else:
            return False, pivot


print(BinarySearcher.binary_search([1, 2, 3], 3))
