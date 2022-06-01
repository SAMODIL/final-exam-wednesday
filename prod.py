"""
Enter your full name here:



Enter your ID here:


"""


def prefix_prod(array):
    """
    Given a list called 'array', return a new list of prefix sums

    Input:
        array (list) - a list of non-zero integers

    Return:
        new_array (list) - a list of integers where new_array[i] is the product
                           of the elements off array up to and including i-th
                           element.

        So, new_array[i] = array[0] * array[1] * ... * array[i]

    Example: if array = [1, 2, 3, 4, 5],
    then you should return [1, 2, 6, 24, 120]

    YOU SHOULD NOT CHANGE ANYTHING IN 'array', BUT INSTEAD
    DO ALL THE WORK ON 'new_array' AND RETURN IT
    """
    prefix_array = [array[0]]


def segment_prod(array, left, right):
    """
    Return the product of the 'array' from the 'left' index all the way until the
    'right' index. 'right' index needs to be included too.

    You MUST use prefix_prod

    Input:
        array (list) - a list of non-zero integers
        left (integer) - a non-negative integer, a valid index in the 'array'
        right (integer) - a non-negative integer, a valid index in the 'array'.
                          It can always be assumed that
                          left <= right

    Return:
        the prod of the elements of 'array' from the 'left' index until 'right'
        index, inluding it in the sum.

        In other words, you should return what
        array[left] * array[left + 1] * ... * array[right - 1] * array[right]
        would be equal to by using the array you get from prefix_sum

    Example:
        Inputs: array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], left = 2, right = 5
        Return: array[2] * array[3] * array[4] * array[5] = 360
    """
    prefix_array = prefix_prod(array)



def max_prod_segment(array):
    """
    Find the maximal product among all subsegments of 'array'

    You MUST use segment_prod

    Input:
        array (list) - a list of non-zero integers
    Return:
        max_prod (int) - the maximal product among every subsegment of 'array'

        If two splittings exist, return the one for which array1 has the least
        amount of elements.

    For example, if array = [1, 2, 4, -1] you must return 1*2*4=8
    """
    pass
