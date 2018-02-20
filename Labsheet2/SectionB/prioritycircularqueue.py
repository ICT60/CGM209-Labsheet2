
from circularqueue import CircularQueue

class PriorityCircularQueue:
    def __init__(self, size, priority_size):
        self._size = size
        self._priority_size = priority_size
        self._queue = [ CircularQueue(size) ]
        for i in range(priority_size - 1):
            self._queue.append(CircularQueue(size))

    def enqueue(self, value, priority_num):
        self._queue[priority_num - 1].enqueue(value)

    def dequeue(self):
        for i in range(self._priority_size):
            if self._queue[i].isEmpty():
                continue
            else:
                self._queue[i].dequeue()
                break

    def size(self):
        return self._size

    def priority_size(self):
        return self._priority_size

    def to_string(self):
        print()
        print("------------------------------")
        print()
        for i in range(self._priority_size):
            print("Priority : ", i + 1)
            self._queue[i].to_string()
        print()
        print("------------------------------")

