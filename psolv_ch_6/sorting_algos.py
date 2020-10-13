import random


def bubble_sort(i_list):
    print(f"Starting bubble sort of {i_list}")
    for passnum in range(len(i_list) - 1, 0, -1):
        print(f"Starting pass: {len(i_list) - passnum}")
        for i in range(passnum):
            if i_list[i] > i_list[i + 1]:
                # temp = i_list[i]
                # i_list[i] = i_list[i + 1]
                # i_list[i + 1] = temp
                i_list[i], i_list[i + 1] = i_list[i + 1], i_list[i]

            print(f"List looks like: {i_list}")


# Side note. The selection sort makes the same number of comparisons as the bubble sort, but makes much fewer
# exchanges.
def selectionSort(i_list):
    print(f"Starting selection sort of {i_list}")
    for fillslot in range(len(i_list) - 1, 0, -1):
        print(f"Looking to fill slot {fillslot} with value {i_list[fillslot]}")
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            print(f"Looking at value {i_list[location]} at location {location}")
            if i_list[location] > i_list[positionOfMax]:
                print(f"New max found, previous: {i_list[positionOfMax]}, new: {i_list[location]}")
                positionOfMax = location

        print(f"Finished looking for this slot, we switch {i_list[fillslot]} with {i_list[positionOfMax]}")
        i_list[fillslot], i_list[positionOfMax] = i_list[positionOfMax], i_list[fillslot]
        print(f"List now looks like {i_list}")


# Insertion sort shifts items greater than the one one currently being considered to the right. Same number of
# comparisons per pass, but since we are not swapping, it is more efficient than the previous sorting algorithms.
# Also other than bubble sort, comparisons always start from the second item on the list because we always start
# our process on the first item.

def insertionSort(i_list):
    print(f"Starting insertion sort for list {i_list}")
    for index in range(1, len(i_list)):
        currentvalue = i_list[index]
        position = index
        print(f"Looking at item: {currentvalue} at position: {position}")

        while position > 0 and i_list[position - 1] > currentvalue:
            print(f"Item: {i_list[position - 1]} at positon {position - 1} is greater than {currentvalue}")
            i_list[position] = i_list[position - 1]
            position = position - 1
            print(f"List now looks like {i_list}")

        print(f"Now we insert item: {currentvalue} at position: {position}")
        i_list[position] = currentvalue
        print(f"List now looks like {i_list}")


def shellSort(i_list):
    print(f"Starting shell sort. List is {i_list}")
    sublistcount = len(i_list) // 2
    while sublistcount > 0:
        print(f"Dividing into {sublistcount} sublists")

        for startposition in range(sublistcount):
            gapInsertionSort(i_list, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", i_list)

        sublistcount = sublistcount // 2


def gapInsertionSort(i_list, start, gap):
    for i in range(start + gap, len(i_list), gap):

        currentvalue = i_list[i]
        position = i

        while position >= gap and i_list[position - gap] > currentvalue:
            i_list[position] = i_list[position - gap]
            position = position - gap

        i_list[position] = currentvalue


def mergeSort(i_list):
    print("Splitting ", i_list)
    if len(i_list) > 1:
        mid = len(i_list) // 2
        lefthalf = i_list[:mid]
        righthalf = i_list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                i_list[k] = lefthalf[i]
                i = i + 1
            else:
                i_list[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            i_list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            i_list[k] = righthalf[j]
            j = j + 1
            k = k + 1

    print("Merging ", i_list)


def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


my_list = [random.randint(1, 100) for _ in range(10)]
# bubble_sort(my_list)
# selectionSort(my_list)
# insertionSort(my_list)
# shellSort(my_list)
mergeSort(my_list)
