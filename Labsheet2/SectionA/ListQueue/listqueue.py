class LinearQueue:
    def __init__(self):
        self._items = []
        self._count = 0

    def enqueue(self, value):
        self._items.append(value)
        print("Enqueue :", "(", value, ")")

    def dequeue(self):
        value = self._items.pop(0)
        print("Dequeue :", "(", value, ")")

    def get_front(self):
        front = self._items[0]
        print("Front : ", front)
        return front

    def count(self):
        return len(self._items)

    def to_string(self):
        if self.count() > 0:
            print("| ", end = '')
            for obj in self._items:
                print(obj, "| ", end = '')
        print()

