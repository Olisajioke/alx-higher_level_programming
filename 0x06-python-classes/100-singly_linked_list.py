#!/usr/bin/python3
"""Module that creates a Class Node a singly linked list"""


class Node:
    """A class representing a Node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The next node in the linked list.

    Methods:
        __init__(self, data, next_node=None): Initializes a new Node instance.

    Raises:
        TypeError: If data is not an integer.
        TypeError: If next_node is not a Node object.
    """
    def __init__(self, data, next_node=None):
        """Initialize a new Node instance.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional):
            The next node in the linked list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: The data stored in the node."""
        return self._data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Node: The next node in the linked list."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """A class representing a singly linked list.

    Attributes:
        head (Node): The first node in the linked list.

    Methods:
        __init__(self): Initializes a new SinglyLinkedList instance.
        sorted_insert(self, value): Inserts a new node in sorted order.

    """
    def __init__(self):
        """Initialize a new SinglyLinkedList instance."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new node in sorted order.

        Args:
            value (int): The value to be inserted into the linked list.
        """
        new_node = Node(value)

        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current_node = self.head
        while current_node.next_node and current_node.next_node.data < value:
            current_node = current_node.next_node

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
