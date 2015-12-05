import random

def quicksort(list, left_bound=0, right_bound=None):
    """
    Sorts a list in place by recursively partitioning the list. Each partition orders a smaller subarray and produces new subarrays to partition.

    :param list list: An unordered list containing comparable elements.
    :param int left_bound: Index for left bound of subarray.
    :param int right_bound: Index for right bound of subarray.
    :returns: An ordered list.
    """
    if not right_bound:
        random.shuffle(list) # randomly sort on first call to prevent worst case scenario
        right_bound = len(list) - 1 # right_bound is the last index on the first call

    if right_bound - left_bound < 2:
        return list # done recursing when the subarray has 1 element

    (lt_subarray_bounds, gt_subarray_bounds) = partition(list, left_bound, right_bound)

    quicksort(list, lt_subarray_bounds[0], lt_subarray_bounds[1])
    quicksort(list, gt_subarray_bounds[0], gt_subarray_bounds[1])

    return list

def partition(list, left_bound, right_bound):
    """
    Partition a subarray into two subarrays, one with values less than a pivot and one with values greater than a pivot. The subbarray is also ordered by swapping elements when out of place in relation to the pivot.

    :param list list: An unordered list containing comparable elements.
    :param int left_bound: Index for left bound of subarray.
    :param int right_bound: Index for right bound of subarray.
    :returns: A tuple of tuples representing new bounds for each new partition.
    """
    pivot = list[left_bound]
    new_bound = left_bound + 1
    for next_unsorted in range(left_bound + 1, right_bound + 1):
        if list[next_unsorted] < pivot:
            # move next_unsorted with the smaller els
            temp = list[next_unsorted]
            list[next_unsorted] = list[new_bound]
            list[new_bound] = temp
            new_bound += 1
    # swap pivot and the last of the smaller els
    temp = list[left_bound] # pivot location
    list[left_bound] = list[new_bound - 1]
    list[new_bound - 1] = temp

    return ((left_bound, new_bound - 1), (new_bound, right_bound))

list = [ 1, 2, 9, 5, 4, 6, 7, 3, 0, 100, -100, 10000 ]
print quicksort(list)







