#!/usr/bin/python3

from queueadjustitem import LinearQueue


class App:
    def __init__(self):
        self._queue = LinearQueue(5)

    def run(self):
        print("------------------------------")
        print()
        self._queue.enqueue(25)
        self._queue.to_string()

        print()
        self._queue.enqueue(2)
        self._queue.to_string()

        print()
        self._queue.enqueue(35)
        self._queue.to_string()

        print()
        self._queue.dequeue()
        self._queue.to_string()

        print()
        self._queue.enqueue(8)
        self._queue.to_string()

        print()
        self._queue.dequeue()
        self._queue.to_string()

        print()
        self._queue.dequeue()
        self._queue.to_string()

        print()
        self._queue.dequeue()
        self._queue.to_string()

        print()
        self._queue.enqueue(12)
        self._queue.to_string()

        print()
        self._queue.enqueue(3)
        self._queue.to_string()

        print()
        print("------------------------------")
        print("Result : ")
        self._queue.to_string()

        print()
        print("Remaining Item :", self._queue.count())
        print()

        print("------------------------------")
        input("Press any key to exit....")


if __name__ == "__main__":
    app = App()
    app.run()
