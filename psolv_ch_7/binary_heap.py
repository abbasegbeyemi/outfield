# New ADT alert introducing the Binary Heap

class BinaryHeap:
    def __init__(self):
        self.heaplist = [0]
        self.currentSize = 0

    def insert(self, value):
        self.heaplist.append(value)
        self.currentSize += self.currentSize
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                self.heaplist[i], self.heaplist[i // 2] = self.heaplist[i // 2], self.heaplist[i]

        i //= 2

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]

            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2

        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2

            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, i_list):
        i = len(i_list) // 2

        self.currentSize = len(i_list)
        self.heaplist[0] = [0] + i_list[:]

        while (i > 0):
            self.percDown(i)
            i -= 1
