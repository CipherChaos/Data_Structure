class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        current = self.head.next
        outside = ""
        while current:
            outside += f"\n |___ {current.data} ___|"
            current = current.next
        return outside[:]


    def get_size(self):
        return self.size

    def push(self, item):
        node = Node(item)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.is_empty:
            raise Exception("Popping from an empty stack is not possible! ")
        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1
        return remove.data

    def peek(self):

        if self.is_empty:
            return None

        return self.head.next.data

    @property
    def is_empty(self):
        return self.size == 0

def main():
    stack = Stack()

    for data in range(1, 30):
        stack.push(data)

    print(f"Stack is: {stack}")

    for _ in range(8):
        stack.pop()

    print(f"Stack is {stack}")

if __name__ == "__main__":
    main()
