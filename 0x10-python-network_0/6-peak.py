#!/usr/bin/python3
""" Finds Peak values """

def find_peak(list_of_integers):
    # Check if the list is empty
    if not list_of_integers:
        return None

    # Initialize left and right pointers
    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

    # Compare the middle element with its neighbors
        if list_of_integers[mid] > list_of_integers[mid + 1]:

            # If the middle element is greater than its right neighbor,
            # a peak may be in the left half, so move the right pointer
            right = mid
        else:
            # Otherwise, move the left pointer to the right half
            left = mid + 1

    # At the end of the loop, 'left' will be pointing to a peak element
    return list_of_integers[left]
