class BinarySearcher:
    def binary_search(array, number):

        """Returns result of searching number in the array.
        Array must be sorted
        first return says if the number was found, the second - gives the coordinates of the number or the closest to the number"""
        def bin_search(array, l, r, number):
        	if r >= l:

        		m = l + (r - l) / 2

        		if array[m] == number:
        			return m

	        	elif array[m] > number:
    	    		return bin_search(array, l, m - 1, number)

	        	else:
    	    		return bin_search(array, m + 1, number)

    	    else:
    	    	return r

print(BinarySearcher.binary_search([1, 2, 3], 3))