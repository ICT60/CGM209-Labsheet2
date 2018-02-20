class CircularQueue:
    def __init__(self, size):
        self._frontIndex = 0
        self._rearIndex = 0
        self._items = [None] * size
        self._count = 0

    def enqueue(self, value):
        if self._rearIndex < self.size() and not self.isFull():
            self._items[self._rearIndex] = value
            self._rearIndex += 1
            self._count += 1

            if self._rearIndex == self.size():
                self._rearIndex = 0

            print("Enqueue :", "(", value, ")")
        else:
            # raise Exception("Queue is Overflow")
            print("Try to Enqueue :", "(", value, ")")
            print("Queue is Overflow")

    def dequeue(self):
        if self.count() > 0:
            value = self._items[self._frontIndex]
            self._items[self._frontIndex] = None

            self._frontIndex += 1
            self._count -= 1

            if self._frontIndex == self.size():
                self._frontIndex = 0

            print("Dequeue :", "(", value, ")")
        else:
            # raise Exception("Queue is Underflow")
            print("Queue is Underflow")

    def get_front(self):
        front = self._items[self._frontIndex]
        return front

    def count(self):
        return self._count

    def size(self):
        return len(self._items)

    def isEmpty(self):
        return self.count() == 0

    def isFull(self):
        return self.count() == self.size()

    def to_string(self):
        if self.size() > 0:
            print("| ", end = '')
            for obj in self._items:
                print(obj, "| ", end = '')
        print()
        print("Front Index : ", self._frontIndex)
        print("Rear Index : ", self._rearIndex)
        print()
