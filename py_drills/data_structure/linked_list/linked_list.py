class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def count(self):
        if self.is_empty:
            return 0
        else:
            return sum(1 for _ in self.iter_nodes)

    def insert(self, index, data):

        if self.is_empty:
            print("List is empty! Can't insert at index", index)
            return

        if index == 0:
            self.append(data)
            return

        current_node = self.head
        position = 0
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index is out of range!")

    def remove_first_node(self):

        if self.is_empty:
            print("There is no element to remove")
            return

        self.head = self.head.next

    def remove_last_node(self):

        current_node = self.head

        if self.is_empty:
            print("There is no element to remove")
            return

        while current_node.next is not None and current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    def remove_at_node(self, index):
        current_node = self.head

        if self.is_empty:
            print("List is empty! Can't remove the item at index", index)
            return

        position = 0

        if index == 0:
            self.remove_first_node()
        else:

            while current_node is not None and position != index:
                position += 1
                current_node = current_node.next

            if current_node is None or current_node is None:
                print("Index is out of range!")
            else:
                current_node.next = current_node.next.next

    def clear(self):

        if self.is_empty:
            return
        self.head = None

    def update_node_value(self, index, value):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = value
        else:
            while current_node is not None and position != index:
                position += 1
                current_node = current_node.next
            if current_node is not None:
                current_node.data = value
            else:
                print("Index is out of range!")

    def to_list(self):
        arr = []
        current = self.head

        while current is not None:
            arr.append(current.data)
            current = current.next
        return arr

    def reverse(self):

        if self.is_empty:
            print("The list Cannot be reversed!")
            return

        current_node = self.head
        previous_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return previous_node

    @property
    def iter_nodes(self):
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def is_empty(self, message = True):

        if self.head is None:
            if message:
                print("The list is empty!")
            return True
        return False

    def show(self, end=" -> ", tail=False):
        current_node = self.head
        result = ""
        while current_node:
            result += str(current_node.data)

            if current_node.next:
                result += end

            current_node = current_node.next

        if tail:
            result += f"{end}None"

        return result


def main():
    linked_list = LinkedList()
    linked_list.append(2)
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(8)
    # linked_list.insert(2,1)
    print(linked_list.show())
    linked_list.to_list()
    print(type(linked_list.show()))
    # linked_list.reverse()
    # print(linked_list.count())
    # linked_list.delete_last()
    # linked_list.update_node_value(4, 3)
    # print(linked_list.show(tail=False))

if __name__ == "__main__":
    main()
    #get
    #find
    #method
    #commends should be added in this project