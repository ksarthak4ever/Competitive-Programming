from __future__ import print_function


def bubble_sort(collection):
    length = len(collection)
    for i in range(length):
        swapped = False
        for j in range(length-1):
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if not swapped: break  # Stop iteration if the collection is sorted.
    return collection

if __name__ == '__main__':
    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(bubble_sort(unsorted))