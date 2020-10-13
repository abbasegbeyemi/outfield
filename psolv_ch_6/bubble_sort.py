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


my_list = [random.randint(1, 100) for _ in range(10)]
bubble_sort(my_list)
