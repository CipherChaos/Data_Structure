class Node:
    """A node in a linked list containing data and a reference to the next node."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        """String representation of the node's data."""
        return str(self.data)


class LinkedList:
    """A singly linked list implementation with common operations."""

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def append(self, data):
        """Add a new node with the given data to the end of the list."""
        new_node = Node(data)

        # If list is empty, new node becomes the head
        if self.is_empty:
            self.head = new_node
            return

        # Otherwise, traverse to the end and append
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):
        """Add a new node with the given data to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, index, data):
        """Insert a new node with the given data at the specified index."""
        # Handle empty list
        if self.is_empty:
            if index == 0:
                self.append(data)
                return
            print(f"List is empty! Can't insert at index {index}")
            return

        # Handle insertion at beginning
        if index == 0:
            self.prepend(data)
            return

        # Find the position before the insertion point
        current_node = self.head
        position = 0
        while current_node and position < index - 1:
            position += 1
            current_node = current_node.next

        # Check if index is valid
        if current_node is None:
            print("Index is out of range!")
            return

        # Insert the new node
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node

    def remove_first_node(self):
        """Remove the first node from the list."""
        if self.is_empty:
            print("There is no element to remove")
            return

        self.head = self.head.next

    def remove_last_node(self):
        """Remove the last node from the list."""
        if self.is_empty:
            print("There is no element to remove")
            return

        # If only one node, remove it
        if self.head.next is None:
            self.head = None
            return

        # Find the second-to-last node
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        # Remove the last node
        current_node.next = None

    def remove_at_index(self, index):
        """Remove the node at the specified index."""
        if self.is_empty:
            print(f"List is empty! Can't remove the item at index {index}")
            return

        # Handle removal of first node
        if index == 0:
            self.remove_first_node()
            return

        # Find the node before the one to be removed
        current_node = self.head
        position = 0
        while current_node and position < index - 1:
            position += 1
            current_node = current_node.next

        # Check if index is valid
        if current_node is None or current_node.next is None:
            print("Index is out of range!")
            return

        # Remove the node
        current_node.next = current_node.next.next

    def clear(self):
        """Remove all nodes from the list."""
        self.head = None

    def update_node_value(self, index, value):
        """Update the value of the node at the specified index."""
        if self.is_empty:
            print(f"List is empty! Can't update at index {index}")
            return

        # Find the node to update
        current_node = self.head
        position = 0
        while current_node and position < index:
            position += 1
            current_node = current_node.next

        # Check if index is valid
        if current_node is None:
            print("Index is out of range!")
            return

        # Update the value
        current_node.data = value

    def find(self, value):
        """Find the first node with the given value and return its index, or -1 if not found."""
        if self.is_empty:
            return -1

        current_node = self.head
        position = 0

        while current_node:
            if current_node.data == value:
                return position
            position += 1
            current_node = current_node.next

        return -1  # Value not found

    def get(self, index):
        """Get the data value at the specified index."""
        if self.is_empty:
            print(f"List is empty! Can't get value at index {index}")
            return None

        current_node = self.head
        position = 0

        while current_node and position < index:
            position += 1
            current_node = current_node.next

        if current_node is None:
            print("Index is out of range!")
            return None

        return current_node.data

    def to_list(self):
        """Convert the linked list to a Python list."""
        result = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result

    def reverse(self):
        """Reverse the linked list and return the new head."""
        if self.is_empty:
            print("The list cannot be reversed!")
            return None

        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        # Update head to the new first node (previously the last)
        self.head = previous_node
        return self.head

    def count(self):
        """Return the number of nodes in the list."""
        return len(self.to_list())

    @property
    def iter_nodes(self):
        """Generator to iterate through all nodes."""
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def show(self, end=" -> ", tail=False):
        """Return a string representation of the list."""
        if self.is_empty:
            return "Empty list"

        result = []
        for node in self.iter_nodes:
            result.append(str(node))

        output = end.join(result)

        if tail:
            output += f"{end}None"

        return output

    def __str__(self):
        """String representation of the linked list."""
        return self.show()


def main():
    """Test the LinkedList implementation."""
    # Create a new linked list
    linked_list = LinkedList()

    print("Testing append operations:")
    linked_list.append(2)
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(8)
    print(linked_list.show())

    print("\nTesting prepend operation:")
    linked_list.prepend(1)
    print(linked_list.show())

    print("\nTesting insert operation:")
    linked_list.insert(3, 5)
    print(linked_list.show())

    print("\nConverting to list:")
    print(linked_list.to_list())

    print("\nTesting find operation:")
    print(f"Index of value 6: {linked_list.find(6)}")
    print(f"Index of value 10: {linked_list.find(10)}")

    print("\nTesting get operation:")
    print(f"Value at index 2: {linked_list.get(2)}")

    print("\nTesting update operation:")
    linked_list.update_node_value(2, 9)
    print(f"After updating index 2: {linked_list}")

    print("\nTesting remove operations:")
    linked_list.remove_first_node()
    print(f"After removing first: {linked_list}")

    linked_list.remove_last_node()
    print(f"After removing last: {linked_list}")

    linked_list.remove_at_index(1)
    print(f"After removing at index 1: {linked_list}")

    print("\nTesting reverse operation:")
    linked_list.reverse()
    print(f"After reversing: {linked_list}")

    print("\nCount:", linked_list.count())

    print("\nTesting clear operation:")
    linked_list.clear()
    print(f"After clearing: {linked_list}")


if __name__ == "__main__":
    main()