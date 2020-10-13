class Stack:
    """The stack class which is an abstract data type that appends to and removes from the end of a list"""

    def __init__(self):
        """Constructor for Stack"""
        self._stack_list = []

    def push(self, item):
        self._stack_list.append(item)

    def pop(self):
        return self._stack_list.pop()

    def isEmpty(self):
        return self._stack_list == []

    def peek(self):
        return self._stack_list[len(self._stack_list) - 1]

    def size(self):
        return len(self._stack_list)


class Queue:

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def isEmpty(self):
        return self._items == []

    def size(self):
        return len(self._items)


def hot_potato(name_list, num_count):
    q = Queue()

    for name in name_list:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num_count):
            q.enqueue(q.dequeue())

        print(f"Now removing {q.dequeue()}")

    return q.dequeue()


if __name__ == '__main__':
    nlist = ["Abbas", "Toyyibat", "Abike", "Hafsa", "Noni", "Uche", "Mayowa", "Folake", "Folusho", "Solape", "Folasade"]
    winner = hot_potato(nlist, 6)

    print(f"The winner is: {winner}")
