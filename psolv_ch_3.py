from timeit import Timer

# We want to verify that list index operator is O(1)
# meaning it takes the same time irrespective of how big the list is
# for listSize in range(1000, 100001, 1000):
#     # Create a timer object per list
#     tlist_timer = Timer("tlist[30]", "from __main__ import tlist")
#     tlist = list(range(listSize))
#     # Get the time taken for 1000 iterations
#     time_taken = tlist_timer.timeit(number=1000)
#     print(f"List size: {listSize} | timeTaken: {time_taken} milliseconds")


# We want to verify that get and set for dictionaries are both O(1)
# for dictSize in range(1000, 100001, 1000):
#     # We want to time asetting the 5th dict index to Abbas
#     tdict_set_timer = Timer("tdict[5] = 'Abbas'", "from __main__ import tdict")
#     # We want to get the value of the 5th dictionary index
#     tdict_get_timer = Timer("tdict[5]", "from __main__ import tdict")
#     # Generate the dictionary with the size
#     tdict = {i: "Abbas" for i in range(dictSize)}
#
#     get_time = tdict_get_timer.timeit(number=1000)
#     set_time = tdict_set_timer.timeit(number=1000)
#
#     print(f"List size: {dictSize} | get: {get_time} milliseconds | set: {set_time}")


# We want to text the performance of del on list and dictionaries
for size in range(10000, 1000001, 10000):
    # We want to time asetting the 5th dict index to Abbas
    list_timer = Timer("del tlist[5]", "from __main__ import tlist")
    # We want to get the value of the 5th dictionary index
    dict_timer = Timer("del tdict[len(tdict)-10]", "from __main__ import tdict")
    # Generate the dictionary with the size
    tdict = {i: "Abbas" for i in range(size)}
    tlist = list(range(size))

    list_time = list_timer.timeit(number=1000)
    dict_time = dict_timer.timeit(number=1000)

    print(f"List size: {size} | list: {list_time} milliseconds | dict: {dict_time}")

# We want to write an algorithm that works in O(n log n) to find the kth smallest number in a list

