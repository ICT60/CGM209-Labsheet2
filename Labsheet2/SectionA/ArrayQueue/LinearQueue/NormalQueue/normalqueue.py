
class LinearQueue:
    def __init__(self, size):
        self._frontIndex = 0
        self._rearIndex = 0
        self._items = [None] * size
        self._count = 0

    def enqueue(self, value):
        if self._rearIndex < self.size():
            self._items[self._rearIndex] = value
            self._rearIndex += 1
            self._count += 1
            print("Enqueue :", "(", value, ")")
        else:
            # raise Exception("Queue is Overflow")
            print("Try to Enqueue :", "(", value, ")")
            print("Queue is Overflow")

    def dequeue(self):
        if self._frontIndex < self.size():
            value = self._items[self._frontIndex]
            self._frontIndex += 1
            self._count -= 1
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

    def to_string(self):
        if self.size() > 0:
            print("| ", end = '')
            for obj in self._items:
                print(obj, "| ", end = '')
        print()
        print("Front Index : ", self._frontIndex)
        print("Rear Index : ", self._rearIndex)
        print()

