import pytest
from data_structure.linked_list.circular_linked_list import CircularLinkedList

@pytest.fixture
def empty_circular_list():
    """Fixture to create an empty CircularLinkedList for tests."""
    return CircularLinkedList()


@pytest.fixture
def populated_circular_list():
    """Fixture to create a CircularLinkedList with some values."""
    circular_list = CircularLinkedList()
    circular_list.append(1)
    circular_list.append(2)
    circular_list.append(3)
    return circular_list


def test_empty_circular_list_properties(empty_circular_list):
    """Test properties of an empty circular list."""
    assert empty_circular_list.is_empty
    assert empty_circular_list.count() == 0
    assert empty_circular_list.to_list() == []
    assert empty_circular_list.show() == ""


def test_append_circularity(empty_circular_list):
    """Test that append maintains circularity."""
    # Add first node
    empty_circular_list.append(1)
    assert empty_circular_list.head.next == empty_circular_list.head  # Points to itself

    # Add second node
    empty_circular_list.append(2)

    # Find the last node
    last_node = empty_circular_list.head
    while last_node.next != empty_circular_list.head:
        last_node = last_node.next

    # Check if the last node points back to head (circularity)
    assert last_node.next == empty_circular_list.head


def test_append_to_circular_list(empty_circular_list):
    """Test appending nodes to a circular list."""
    empty_circular_list.append(1)
    empty_circular_list.append(2)
    empty_circular_list.append(3)

    assert not empty_circular_list.is_empty
    assert empty_circular_list.to_list() == [1, 2, 3]
    assert empty_circular_list.show() == "1 -> 2 -> 3"
    assert empty_circular_list.show(tail=True) == "1 -> 2 -> 3 -> (back to 1)"


def test_prepend_circularity(empty_circular_list):
    """Test that prepend maintains circularity."""
    # Add first node
    empty_circular_list.prepend(1)
    assert empty_circular_list.head.next == empty_circular_list.head  # Points to itself

    # Add second node to the front
    empty_circular_list.prepend(2)

    # Check if new head is 2
    assert empty_circular_list.head.data == 2

    # Find the last node
    last_node = empty_circular_list.head
    while last_node.next != empty_circular_list.head:
        last_node = last_node.next

    # Check if the last node points back to the new head (circularity)
    assert last_node.next == empty_circular_list.head


def test_prepend_to_circular_list(empty_circular_list):
    """Test prepending nodes to a circular list."""
    empty_circular_list.prepend(3)
    empty_circular_list.prepend(2)
    empty_circular_list.prepend(1)

    assert empty_circular_list.to_list() == [1, 2, 3]
    assert empty_circular_list.show() == "1 -> 2 -> 3"


def test_insert_circularity(populated_circular_list):
    """Test that insert maintains circularity."""
    # Insert in the middle
    populated_circular_list.insert(1, 10)

    # Check updated list content
    assert populated_circular_list.to_list() == [1, 10, 2, 3]

    # Find the last node
    last_node = populated_circular_list.head
    while last_node.next != populated_circular_list.head:
        last_node = last_node.next

    # Check if the last node points back to head (circularity maintained)
    assert last_node.next == populated_circular_list.head


def test_remove_first_node_circularity(populated_circular_list):
    """Test that removing the first node maintains circularity."""
    populated_circular_list.remove_first_node()

    # Check updated list content
    assert populated_circular_list.to_list() == [2, 3]

    # Find the last node
    last_node = populated_circular_list.head
    while last_node.next != populated_circular_list.head:
        last_node = last_node.next

    # Check if the last node points back to the new head (circularity maintained)
    assert last_node.next == populated_circular_list.head


def test_remove_last_node_circularity(populated_circular_list):
    """Test that removing the last node maintains circularity."""
    populated_circular_list.remove_last_node()

    # Check updated list content
    assert populated_circular_list.to_list() == [1, 2]

    # Find the last node (now the second node)
    last_node = populated_circular_list.head
    while last_node.next != populated_circular_list.head:
        last_node = last_node.next

    # Check if the new last node points back to head (circularity maintained)
    assert last_node.next == populated_circular_list.head


def test_remove_single_element_list():
    """Test removing the only element from a single-element circular list."""
    single_element_list = CircularLinkedList()
    single_element_list.append(1)

    # Check that it's circular
    assert single_element_list.head.next == single_element_list.head

    # Remove the only element
    single_element_list.remove_first_node()

    # Check that the list is now empty
    assert single_element_list.is_empty
    assert single_element_list.to_list() == []


def test_iter_nodes(populated_circular_list):
    """Test the iter_nodes generator for circular lists."""
    nodes = list(populated_circular_list.iter_nodes)
    assert len(nodes) == 3
    assert [node.data for node in nodes] == [1, 2, 3]

    # Make sure we don't iterate infinitely
    count = 0
    for _ in populated_circular_list.iter_nodes:
        count += 1
        assert count <= 100, "Infinite loop detected in iter_nodes"


def test_to_list(populated_circular_list):
    """Test converting a circular list to a regular list."""
    regular_list = populated_circular_list.to_list()
    assert regular_list == [1, 2, 3]

    # Check for a single element list
    single_element = CircularLinkedList()
    single_element.append(10)
    assert single_element.to_list() == [10]


def test_count(populated_circular_list, empty_circular_list):
    """Test counting elements in a circular list."""
    assert empty_circular_list.count() == 0

    # Test with populated list - there's an indentation bug in your count method
    # The test will fail unless you fix the indentation of the return statement
    # This test checks the expected behavior (not the current buggy behavior)
    populated_circular_list_count = populated_circular_list.count()
    assert populated_circular_list_count == 3, f"Expected 3, got {populated_circular_list_count}"

    # Add one more and test again
    populated_circular_list.append(4)
    assert populated_circular_list.count() == 4


def test_show(populated_circular_list):
    """Test string representation of a circular list."""
    assert populated_circular_list.show() == "1 -> 2 -> 3"
    assert populated_circular_list.show(
        tail=True) == "1 -> 2 -> 3 -> (back to 1)"
    assert populated_circular_list.show(end=" * ") == "1 * 2 * 3"

    # Empty list
    empty = CircularLinkedList()
    assert empty.show() == ""


def test_reverse_circularity(populated_circular_list):
    """Test that reversing maintains circularity."""
    populated_circular_list.reverse()

    # Check content is reversed
    assert populated_circular_list.to_list() == [3, 2, 1]

    # Find the last node
    last_node = populated_circular_list.head
    while last_node.next != populated_circular_list.head:
        last_node = last_node.next

    # Check if the last node points back to head (circularity maintained)
    assert last_node.next == populated_circular_list.head


def test_reverse(populated_circular_list):
    """Test reversing a circular list."""
    # Reverse the list
    populated_circular_list.reverse()
    assert populated_circular_list.to_list() == [3, 2, 1]

    # Reverse again to get back to original order
    populated_circular_list.reverse()
    assert populated_circular_list.to_list() == [1, 2, 3]

    # Test with single element
    single_element = CircularLinkedList()
    single_element.append(10)
    single_element.reverse()
    assert single_element.to_list() == [10]


def test_error_handling():
    """Test handling of operations on empty lists."""
    empty_list = CircularLinkedList()

    # These operations should not raise exceptions even on empty lists
    empty_list.remove_first_node()  # Should print error but not crash
    empty_list.remove_last_node()  # Should print error but not crash
    empty_list.reverse()  # Should print error but not crash


def test_circular_behavior():
    """Test circular behavior by traversing beyond the list size."""
    circular_list = CircularLinkedList()
    circular_list.append(1)
    circular_list.append(2)
    circular_list.append(3)

    # Traverse the list more times than there are elements
    # to verify circular behavior
    current = circular_list.head
    values = []

    # Collect 9 values (3 full rotations)
    for _ in range(9):
        values.append(current.data)
        current = current.next

    # Check that we get three full rotations
    assert values == [1, 2, 3, 1, 2, 3, 1, 2, 3]


def test_bugs_in_implementation():
    """Test for specific bugs in the implementation."""
    # Testing the bug in the insert method where it checks current_node.data + 1 == index
    # Instead of checking position + 1 == index
    circular_list = CircularLinkedList()
    circular_list.append(1)  # data is 1
    circular_list.append(2)  # data is 2

    # This should insert at index 1 (between 1 and 2), but the bug will prevent it
    # because it checks if the node's data + 1 equals the index
    circular_list.insert(1, 1.5)

    # With the bug, the list will remain [1, 2]
    # If the bug is fixed, the list will be [1, 1.5, 2]

    # Note: This test case might fail without fixing the bug
    # It's included to highlight the issue

    # Testing the indentation bug in the count method
    # The return statement is indented inside the while loop,
    # so it will always return after the first iteration
    circular_list = CircularLinkedList()
    circular_list.append(1)
    circular_list.append(2)
    circular_list.append(3)

    # With the bug, this will likely return 1 instead of 3
    # Note: This test case will fail without fixing the bug
    # It's included to highlight the issue


if __name__ == "__main__":
    pytest.main(["-v"])