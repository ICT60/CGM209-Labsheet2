#!/usr/bin/python3
from circularqueue import CircularQueue
from prioritycircularqueue import PriorityCircularQueue

class App:
    def __init__(self):
        self._queue = PriorityCircularQueue(5, 3)

    def run(self):
        self._queue.enqueue('A', 2)
        self._queue.to_string()

        self._queue.enqueue('B', 3)
        self._queue.to_string()

        self._queue.enqueue('C', 1)
        self._queue.to_string()

        self._queue.dequeue()
        self._queue.to_string()

        self._queue.enqueue('D', 2)
        self._queue.to_string()

        self._queue.dequeue()
        self._queue.to_string()

        self._queue.dequeue()
        self._queue.to_string()

        self._queue.enqueue('E', 1)
        self._queue.to_string()

        self._queue.enqueue('F', 1)
        self._queue.to_string()

        self._queue.dequeue()
        self._queue.to_string()

        self._queue.enqueue('G', 3)
        self._queue.to_string()

        self._queue.enqueue('H', 2)
        self._queue.to_string()

        input("Press any key to exit....")


if __name__ == "__main__":
    app = App()
    app.run()
