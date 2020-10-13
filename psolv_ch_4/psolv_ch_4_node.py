# Implementation of the npde class which is a basic building block of the linked list

class Node:
    def __init__(self, init_data, index):
        self._data = init_data
        self._next = None
        self._index = index

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self.index = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value

    def __str__(self):
        return f"Node: value: {self.data} | next: {self.next}"

    def __repr__(self):
        return f"Node: value: {self.data} | next: {self.next}"


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, node_val):
        tmp = Node(node_val, 0)
        tmp.next = self.head
        if self.head is None:
            self.tail = tmp
        self.head = tmp

    def size(self):
        # To count the list we use linked list traversal
        count = 0
        next_node = self.head
        while next_node is not None:
            count += 1
            next_node = next_node.next

        return count

    def search(self, value):
        # Same traversal technique for searching through a linked list
        found = False
        current_node = self.head
        count = 0
        while (current_node is not None) and not found:
            found = current_node.data == value
            if not found:
                current_node = current_node.next
                count += 1

        return count if found else None

    def remove(self, value):
        # This one is a bit more tricky beause we need to remove a node by connecting the
        # previous node to the node after the one we want to remove
        found = False
        current_node = self.head
        previous_node = None

        while (current_node is not None) and not found:
            found = current_node.data == value

            if found and (previous_node is not None):
                previous_node.next = current_node.next

            elif found and (previous_node is None):
                self.head = current_node.next

            else:
                previous_node = current_node
                current_node = current_node.next

            if found and (current_node.next is None):
                self.tail = None if self.head is None else previous_node

    def append(self, value):
        # We want to inplement a method that appends to the list. This is an O(n) solution
        if self.head is None:
            self.add(value)
        else:
            tmp = Node(value)
            self.tail.next = tmp
            self.tail = tmp
        #     current_node = self.head
        #     previous_node = None
        #     while current_node is not None:
        #         previous_node = current_node
        #         current_node = current_node.next
        #
        #     previous_node.next = Node(value)

    def insert(self, value, index):
        pass


if __name__ == '__main__':
    ls = UnorderedList()

    ls.add(2)
    ls.add("abbas")
    ls.add(3)
    ls.add("indigo")
    ls.add(22)
    ls.add(1738)
    print(ls.head)
    print(ls.tail)
    print(ls.size())
    print(ls.search("abbas"))
    print(ls.search("toyibat"))
    print(ls.search(1738))
    ls.remove(22)
    ls.remove("indigo")
    ls.remove(1738)
    ls.remove(2)
    print(ls.size())
    ls.append("ruki")
    ls.remove(2)
    print(ls.tail)
    print(ls.head)
    print(ls.size())
