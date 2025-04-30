# def simple_hash(string, table_size=10):
#     result = 0
#     for i, char in enumerate(string):
#         result += ord(char) * (i + 1)
#     return result % table_size
#
#
# def main():
#     string = input("Please enter a string: ")
#     index = simple_hash(string)
#
#     hash_table = [[] for _ in range(10)]
#     hash_table[index].append(string)
#
#     print("Hash table:")
#     for i, bucket in enumerate(hash_table):
#         print(f"{i}: {bucket}")
#
# if __name__ == "__main__":
#     main()

class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def clear(self):
        return self.items.clear()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        if not self.items:
            return True
        else:
            return False


class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()


stack = Stack()

stack.push("apple")
stack.push("banana")
stack.pop()
stack.push("cucumber")
stack.push("cherry")
stack.push("watermelon")

print(stack)

