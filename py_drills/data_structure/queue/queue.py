class Queue:

    def __init__(self):
        self.queue = []
        self.size = 0

    def __str__(self):
        return " -> ".join(str(item) for item in self.queue)

    def enqueue_front(self, item):
        self.queue.insert(0, item)
        self.size += 1

    def enqueue_back(self, item):
        self.queue.append(item)
        self.size += 1

    def dequeue_front(self):
        if not self.is_empty:
            self.size -= 1
            return self.queue.pop(0)
        else:
            raise Exception("The queue is empty! ")

    def dequeue_back(self):
        if not self.is_empty:
            self.size -= 1
            return self.queue.pop()
        else:
            raise Exception("The queue is empty! ")

    def get_size(self):
        return self.size

    @property
    def is_empty(self):
        return self.size == 0


def main():
    queue = Queue()

    queue.enqueue_back(2)
    queue.enqueue_back(5)
    queue.enqueue_front(11)
    queue.enqueue_front(-2)
    queue.enqueue_back(90)

    queue.dequeue_back()
    queue.dequeue_front()

    print(queue.__str__())


if __name__ == "__main__":
    main()
