#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_sortd = list(a_dictionary.keys())
    list_sortd.sort()
    for i in list_sortd:
        print("{}: {}".format(i, a_dictionary.get(i)))
