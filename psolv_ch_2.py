# Two python functions to find the minumum number in a list
from random import randint
import time


def non_linear(number_list):
    smallest = number_list[0]
    for n in number_list:
        for c in number_list:
            if c < n and c < smallest:
                smallest = c

    return smallest


def linear(number_list):
    smallest = number_list[0]
    for n in number_list:
        if n < smallest:
            smallest = n

    return smallest


if __name__ == '__main__':
    listSizes = range(1000, 10001, 1000)
    for listSize in listSizes:
        n_list = [randint(0, 1000000) for _ in range(listSize)]
        start = time.time()
        res = linear(n_list)
        end = time.time()
        print(f"Smallest number is {res} | list size is {listSize} | time taken is {end - start}")
