class Node:
    """A node in a doubly linked list containing data and references to the next and previous nodes."""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        """String representation of the node's data."""
        return str(self.data)


class DoublyLinkedList:
    """A doubly linked list implementation with common operations."""

    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None
        self.tail = None

    def append(self, data):
        """Add a new node with the given data to the end of the list."""
        new_node = Node(data)

        # If list is empty, new node becomes both head and tail
        if self.is_empty:
            self.head = new_node
            self.tail = new_node
            return

        # Otherwise, append after tail and update tail
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        """Add a new node with the given data to the beginning of the list."""
        new_node = Node(data)

        # If list is empty, new node becomes both head and tail
        if self.is_empty:
            self.head = new_node
            self.tail = new_node
            return

        # Otherwise, prepend before head and update head
        new_node.next = self.head
        self.head.prev = new_node
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

        # Handle insertion at end
        if index >= self.count():
            self.append(data)
            return

        # Find the position at the insertion point
        current_node = self.head
        position = 0
        while current_node and position < index:
            position += 1
            current_node = current_node.next

        # Insert the new node before current_node
        new_node = Node(data)
        new_node.prev = current_node.prev
        new_node.next = current_node
        current_node.prev.next = new_node
        current_node.prev = new_node

    def remove_first_node(self):
        """Remove the first node from the list."""
        if self.is_empty:
            print("There is no element to remove")
            return

        # If only one node, clear the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        # Remove the head node and update head
        self.head = self.head.next
        self.head.prev = None

    def remove_last_node(self):
        """Remove the last node from the list."""
        if self.is_empty:
            print("There is no element to remove")
            return

        # If only one node, clear the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        # Remove the tail node and update tail
        self.tail = self.tail.prev
        self.tail.next = None

    def remove_at_index(self, index):
        """Remove the node at the specified index."""
        if self.is_empty:
            print(f"List is empty! Can't remove the item at index {index}")
            return

        # Handle removal of first node
        if index == 0:
            self.remove_first_node()
            return

        # Handle removal of last node if we know the index is the last
        if index == self.count() - 1:
            self.remove_last_node()
            return

        # Find the node to be removed
        current_node = self.head
        position = 0
        while current_node and position < index:
            position += 1
            current_node = current_node.next

        # Check if index is valid
        if current_node is None:
            print("Index is out of range!")
            return

        # Remove the node by updating surrounding links
        current_node.prev.next = current_node.next
        if current_node.next:  # This check is technically redundant given the earlier checks
            current_node.next.prev = current_node.prev

    def clear(self):
        """Remove all nodes from the list."""
        self.head = None
        self.tail = None

    def _get_node_at_index(self, index):
        """
        Helper method to get node at index using optimized traversal.
        Returns the node at the given index or None if index is out of range.
        """
        if self.is_empty:
            return None

        # Optimize retrieval by starting from nearest end
        if index <= self.count() // 2:
            # Start from head for first half
            current_node = self.head
            position = 0
            while current_node and position < index:
                position += 1
                current_node = current_node.next
        else:
            # Start from tail for second half
            current_node = self.tail
            position = self.count() - 1
            while current_node and position > index:
                position -= 1
                current_node = current_node.prev

        return current_node

    def update_node_value(self, index, value):
        """Update the value of the node at the specified index."""
        if self.is_empty:
            print(f"List is empty! Can't update at index {index}")
            return

        # Find the node to update using optimized traversal
        current_node = self._get_node_at_index(index)

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

        # Find the node using optimized traversal
        current_node = self._get_node_at_index(index)

        if current_node is None:
            print("Index is out of range!")
            return None

        return current_node.data

    def to_list(self):
        """Convert the doubly linked list to a Python list."""
        result = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result

    def reverse(self):
        """Reverse the doubly linked list and return the new head."""
        if self.is_empty:
            print("The list cannot be reversed!")
            return None

        # Swap next and prev pointers for all nodes
        current_node = self.head
        while current_node:
            # Swap next and prev
            temp = current_node.next
            current_node.next = current_node.prev
            current_node.prev = temp

            # Move to the next node (which is now current.prev due to swap)
            current_node = current_node.prev

        # Swap head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp

        return self.head

    def count(self):
        """Return the number of nodes in the list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    @property
    def iter_nodes(self):
        """Generator to iterate through all nodes from head to tail."""
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def iter_nodes_reverse(self):
        """Generator to iterate through all nodes from tail to head."""
        current = self.tail
        while current:
            yield current
            current = current.prev

    @property
    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def show(self, end=" <-> ", tail=False):
        """Return a string representation of the list from head to tail."""
        if self.is_empty:
            return "Empty list"

        result = []
        for node in self.iter_nodes:
            result.append(str(node))

        output = end.join(result)

        if tail:
            output = f"None{end}" + output + f"{end}None"

        return output

    def show_reverse(self, end=" <-> ", tail=False):
        """Return a string representation of the list from tail to head."""
        if self.is_empty:
            return "Empty list"

        result = []
        for node in self.iter_nodes_reverse:
            result.append(str(node))

        output = end.join(result)

        if tail:
            output = f"None{end}" + output + f"{end}None"

        return output

    def __str__(self):
        """String representation of the doubly linked list."""
        return self.show()


def main():
    """Test the DoublyLinkedList implementation."""
    # Create a new doubly linked list
    doubly_linked_list = DoublyLinkedList()

    print("Testing append operations:")
    doubly_linked_list.append(2)
    doubly_linked_list.append(6)
    doubly_linked_list.append(7)
    doubly_linked_list.append(8)
    print(doubly_linked_list.show())

    print("\nTesting prepend operation:")
    doubly_linked_list.prepend(1)
    print(doubly_linked_list.show())

    print("\nTesting insert operation:")
    doubly_linked_list.insert(3, 5)
    print(doubly_linked_list.show())

    print("\nConverting to list:")
    print(doubly_linked_list.to_list())

    print("\nTesting find operation:")
    print(f"Index of value 6: {doubly_linked_list.find(6)}")
    print(f"Index of value 10: {doubly_linked_list.find(10)}")

    print("\nTesting get operation:")
    print(f"Value at index 2: {doubly_linked_list.get(2)}")

    print("\nTesting update operation:")
    doubly_linked_list.update_node_value(2, 9)
    print(f"After updating index 2: {doubly_linked_list}")

    print("\nTesting remove operations:")
    doubly_linked_list.remove_first_node()
    print(f"After removing first: {doubly_linked_list}")

    doubly_linked_list.remove_last_node()
    print(f"After removing last: {doubly_linked_list}")

    doubly_linked_list.remove_at_index(1)
    print(f"After removing at index 1: {doubly_linked_list}")

    print("\nTesting reverse operation:")
    doubly_linked_list.reverse()
    print(f"After reversing: {doubly_linked_list}")

    print("\nTesting reverse traversal:")
    print(f"Reverse order: {doubly_linked_list.show_reverse()}")

    print("\nCount:", doubly_linked_list.count())

    print("\nTesting clear operation:")
    doubly_linked_list.clear()
    print(f"After clearing: {doubly_linked_list}")


if __name__ == "__main__":
    main()