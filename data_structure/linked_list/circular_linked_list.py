from linked_list import LinkedList, Node

class CircularLinkedList(LinkedList):
    """
    A circular linked list implementation that inherits from LinkedList.
    In a circular linked list, the last node point back to the head node.
    """

    def __init__(self):
        super().__init__()

    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            #Make it circular by pointing to itself
            new_node.next = new_node
            return

        current_node = self.head
        #Find the last node (the node that point to head)
        while current_node.next and current_node.next != self.head:

            # Update the last node to point to the new node
            current_node = current_node.next
            # Make it circular
            new_node.next = self.head

        current_node.next = new_node

    def prepend(self, data):
        """Add a new node at the beginning and update the last node to point to it"""

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            # Make it circular
            new_node.next = self.head
            return
        #Find the last node
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next

        # Update new node to point to current head
        new_node.next = self.head
        # Update the last node to point to the new head
        current_node.next = new_node
        # Update head pointer again
        self.head = new_node

    def insert(self, index, data):
        """
        Insert a node at the specified index
        """

        if self.is_empty:
            print("List is empty! Can't insert at index", index)
            return

        if index == 0:
            self.append(data)
            return

        current_node = self.head
        position = 0

        while current_node.next != self.head and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node.data + 1 == index:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index is out of range!")

    def remove_first_node(self):

        if self.is_empty:
            print("There is no element to remove")
            return

        if self.head.next == self.head: # If we only have one node
            self.head = None
            return

        current_node = self.head

        while current_node.next != self.head:
            current_node = current_node.next

        # Update the last node to point to the new head
        current_node.next = self.head.next
        # Update head
        self.head = self.head.next

    def remove_last_node(self):
        """
        Remove the last node and update the second-to-last to point to head
        """
        if self.is_empty:
            print("There is no element to remove")
            return

        if self.head.next == self.head:  # Only one node
            self.head = None
            return

        current_node = self.head

        # Find the second-to-last node
        while current_node.next.next != self.head:
            current_node = current_node.next

        # Update the second-to-last node to point to head
        current_node.next = self.head

    @property
    def iter_nodes(self):
        """Generator to iterate through all nodes once"""
        if self.head is not None:
            current = self.head
            yield current
            current = current.next

            # Continue until we reach the head again
            while current != self.head:
                yield current
                current = current.next

    def to_list(self):
        """Convert circular linked list to a regular list"""
        arr = []

        if self.head is None:
            return arr

        current = self.head
        arr.append(current.data)
        current = current.next

        # Continue until we reach the head again
        while current != self.head:
            arr.append(current.data)
            current = current.next

        return arr

    def count(self):
        """Count the number of nodes in the circular list"""
        if self.is_empty:
            return 0

        count = 1  # Start with 1 for the head
        current = self.head.next

        # Count until we reach the head again
        while current != self.head:
            count += 1
            current = current.next

            return count

    def show(self, end=" -> ", tail=False):
        """Display the circular linked list, avoiding infinite loops"""
        if self.is_empty:
            return ""

        result = str(self.head.data)
        current_node = self.head.next

        # Continue until we reach the head again
        while current_node != self.head:
            result += end + str(current_node.data)
            current_node = current_node.next

        if tail:
            result += f"{end}(back to {self.head.data})"

        return result

    def reverse(self):
        """Reverse the circular linked list"""
        if self.is_empty:
            print("The list Cannot be reversed!")
            return

        if self.head.next == self.head:  # Only one node
            return self.head

        prev_node = None
        current_node = self.head
        next_node = None

        # Store the original head to update its next pointer at the end
        original_head = self.head

        # Reverse all nodes
        while True:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

            if current_node == self.head:
                break

        # Update the head to the new head (previously the tail)
        self.head = prev_node

        # Connect the original head (now the tail) to the new head to maintain circularity
        original_head.next = self.head

        return self.head

def main():
    # Test the CircularLinkedList implementation
    circular_list = CircularLinkedList()
    circular_list.append(1)
    circular_list.append(2)
    circular_list.append(3)
    circular_list.append(4)

    print("Circular List:", circular_list.show(tail=True))
    print("Count:", circular_list.count())
    print("As List:", circular_list.to_list())

    print("\nAfter prepending 0:")
    circular_list.prepend(0)
    print("Circular List:", circular_list.show(tail=True))

    print("\nAfter inserting 2.5 at index 3:")
    circular_list.insert(3, 5)
    print("Circular List:", circular_list.show(tail=True))

    print("\nAfter removing first node:")
    circular_list.remove_first_node()
    print("Circular List:", circular_list.show(tail=True))

    print("\nAfter removing last node:")
    circular_list.remove_last_node()
    print("Circular List:", circular_list.show(tail=True))

    print("\nAfter reversing:")
    circular_list.reverse()
    print("Circular List:", circular_list.show(tail=True))

if __name__ == "__main__":
    main()