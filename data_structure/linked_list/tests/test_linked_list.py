import pytest
from data_structure.linked_list.linked_list import LinkedList


@pytest.fixture
def empty_list():
    """Fixture to create an empty LinkedList for tests."""
    return LinkedList()


@pytest.fixture
def populated_list():
    """Fixture to create a LinkedList with some values."""
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    return linked_list


def test_empty_list_properties(empty_list):
    """Test properties of an empty list."""
    assert empty_list.is_empty
    assert empty_list.count() == 0
    assert empty_list.to_list() == []
    assert empty_list.show() == "Empty list"


def test_append(empty_list):
    """Test the append method."""
    empty_list.append(1)
    empty_list.append(2)
    empty_list.append(3)

    assert not empty_list.is_empty
    assert empty_list.count() == 3
    assert empty_list.to_list() == [1, 2, 3]
    assert empty_list.show() == "1 -> 2 -> 3"
    assert empty_list.show(tail=True) == "1 -> 2 -> 3 -> None"


def test_prepend(empty_list):
    """Test the prepend method."""
    empty_list.prepend(3)
    empty_list.prepend(2)
    empty_list.prepend(1)

    assert empty_list.to_list() == [1, 2, 3]
    assert empty_list.show() == "1 -> 2 -> 3"


def test_insert(empty_list):
    """Test the insert method in various scenarios."""
    # Insert into empty list
    empty_list.insert(0, 10)
    assert empty_list.to_list() == [10]

    # Insert at beginning
    empty_list.insert(0, 5)
    assert empty_list.to_list() == [5, 10]

    # Insert in middle
    empty_list.insert(1, 7)
    assert empty_list.to_list() == [5, 7, 10]

    # Insert at end
    empty_list.insert(3, 15)
    assert empty_list.to_list() == [5, 7, 10, 15]

    # Insert out of range (should print error message but not crash)
    empty_list.insert(10, 100)
    assert empty_list.to_list() == [5, 7, 10,
                                    15]  # List should remain unchanged


def test_remove_first_node(empty_list, populated_list):
    """Test removing the first node in various scenarios."""
    # Remove from empty list (should print error message but not crash)
    empty_list.remove_first_node()
    assert empty_list.is_empty

    # Remove from list with one element
    one_element = LinkedList()
    one_element.append(1)
    one_element.remove_first_node()
    assert one_element.is_empty

    # Remove from list with multiple elements
    populated_list.remove_first_node()
    assert populated_list.to_list() == [2, 3]


def test_remove_last_node(empty_list, populated_list):
    """Test removing the last node in various scenarios."""
    # Remove from empty list (should print error message but not crash)
    empty_list.remove_last_node()
    assert empty_list.is_empty

    # Remove from list with one element
    one_element = LinkedList()
    one_element.append(1)
    one_element.remove_last_node()
    assert one_element.is_empty

    # Remove from list with multiple elements
    populated_list.remove_last_node()
    assert populated_list.to_list() == [1, 2]


def test_remove_at_index(populated_list):
    """Test removing a node at a specific index."""
    # Remove first node
    list_copy = LinkedList()
    for item in populated_list.to_list():
        list_copy.append(item)
    list_copy.remove_at_index(0)
    assert list_copy.to_list() == [2, 3]

    # Remove middle node
    list_copy = LinkedList()
    for item in populated_list.to_list():
        list_copy.append(item)
    list_copy.remove_at_index(1)
    assert list_copy.to_list() == [1, 3]

    # Remove last node
    list_copy = LinkedList()
    for item in populated_list.to_list():
        list_copy.append(item)
    list_copy.remove_at_index(2)
    assert list_copy.to_list() == [1, 2]

    # Remove at invalid index (should print error message but not crash)
    list_copy = LinkedList()
    for item in populated_list.to_list():
        list_copy.append(item)
    list_copy.remove_at_index(10)
    assert list_copy.to_list() == [1, 2, 3]  # List should remain unchanged


def test_clear(populated_list):
    """Test clearing the list."""
    populated_list.clear()
    assert populated_list.is_empty
    assert populated_list.count() == 0
    assert populated_list.to_list() == []


def test_update_node_value(populated_list):
    """Test updating a node's value."""
    # Update first node
    populated_list.update_node_value(0, 10)
    assert populated_list.to_list() == [10, 2, 3]

    # Update middle node
    populated_list.update_node_value(1, 20)
    assert populated_list.to_list() == [10, 20, 3]

    # Update last node
    populated_list.update_node_value(2, 30)
    assert populated_list.to_list() == [10, 20, 30]

    # Update at invalid index (should print error message but not crash)
    populated_list.update_node_value(10, 100)
    assert populated_list.to_list() == [10, 20,
                                        30]  # List should remain unchanged


def test_find(populated_list):
    """Test finding values in the list."""
    assert populated_list.find(1) == 0
    assert populated_list.find(2) == 1
    assert populated_list.find(3) == 2
    assert populated_list.find(4) == -1  # Not found

    # Find in empty list
    empty = LinkedList()
    assert empty.find(1) == -1


def test_get(populated_list):
    """Test getting values at specific indices."""
    assert populated_list.get(0) == 1
    assert populated_list.get(1) == 2
    assert populated_list.get(2) == 3

    # Get at invalid index (should print error message but return None)
    assert populated_list.get(10) is None

    # Get from empty list (should print error message but return None)
    empty = LinkedList()
    assert empty.get(0) is None


def test_reverse(empty_list, populated_list):
    """Test reversing the list."""
    # Reverse empty list
    empty_list.reverse()
    assert empty_list.is_empty

    # Reverse list with one element
    one_element = LinkedList()
    one_element.append(10)
    one_element.reverse()
    assert one_element.to_list() == [10]

    # Reverse list with multiple elements
    populated_list.reverse()
    assert populated_list.to_list() == [3, 2, 1]

    # Double reverse should get back to original order
    populated_list.reverse()
    assert populated_list.to_list() == [1, 2, 3]


def test_iter_nodes(populated_list):
    """Test the iter_nodes generator."""
    nodes = list(populated_list.iter_nodes)
    assert len(nodes) == 3
    assert [node.data for node in nodes] == [1, 2, 3]


def test_str_representation(populated_list):
    """Test the string representation of the list."""
    assert str(populated_list) == "1 -> 2 -> 3"

    # Test empty list string representation
    empty = LinkedList()
    assert str(empty) == "Empty list"


if __name__ == "__main__":
    pytest.main(["-v"])
