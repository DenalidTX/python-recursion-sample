# The merge sort is a standard recursive sorting algorithm. It divides the input list in
# half, sorts each of the two halves, then merges them back together in sorted order. This
# is the most complicated of the three examples here, but it illustrates the type of logic
# that benefits most from recursive calls.
#
# The base case in this function is when the list has length 1. The function assumes that
# the list is not empty.
def sort(numbers):
    size = len(numbers)

    # Handle the base case by returning the single-element array.
    if size == 1:
        return numbers
    # Handle all other cases by dividing the list in half. Make sure to use
    # the same (rounded) index for the split, in case the length of the input
    # list is an odd number.
    else:
        split_index = round(size/2)

        # The fact that we are calling the same method again is what makes
        # this function recursive. The call to the merge() function is not
        # recursive, despite the fact that we call it within the recursive
        # calls to sort().
        return merge(sort(numbers[:split_index]), sort(numbers[split_index:]))


# This function merges two sorted lists into a new sorted list containing all elements
# from both input lists.
def merge(list1, list2):
    # Create a new list and iterate through both input lists simultaneously. In each
    # iteration of the while loop take the smaller of the first elements from each
    # input list. Since the input lists are assumed to be sorted, this results in
    # a sorted output list.
    new_list = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            # If the first list's first item is smaller, put it into the new list
            # and remove it from the first input list.
            new_list.append(list1.pop(0))
        else:
            # Otherwise put the second list's first item into the new list and remove
            # it from the second input list.
            new_list.append(list2.pop(0))

    # After the loop has run, one of the loops may have remaining items.
    # Add those items. Only one of the two lists should have anything,
    # but we only know which based on the remaining length.
    if len(list1) > 0:
        new_list.extend(list1)
    if len(list2) > 0:
        new_list.extend(list2)

    return new_list


# Run a few test cases.
print(sort([65, 15, 8, 2, 49, 5, 68, 4, 78, 3, 215, 65, 48, 5]))
print(sort([167, 16789, 4156, 1789, 7986, 168, 614, 81, 168, 76, 71, 1786, 276, 245, 65978, 3224, 78]))
print(sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
print(sort([0, 1, 2 ,3, 4, 5, 6, 7, 8, 9]))
