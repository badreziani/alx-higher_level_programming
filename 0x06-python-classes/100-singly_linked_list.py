#!/usr/bin/python3
"""This file contains a definition for:

- Class 'Node' which defines a node of singly linked list
- Class 'SinglyLinkedList' which defines a singly linked list

"""

class Node:
    """Class Node

    Attribues :
        data: the data of the list
        next_node : the next node
    """
    
    def __init__(self, data, next_node=None):
        """__init__ the constrcutor of the class.
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter method for data attribute.
        """

        return self.__data
    @data.setter
    def data(self, value):
        """Setter method for data attribute.

        Returns:
            the value of data
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value


    @property
    def next_node(self):
        """Getter method for next_node attribue.

        Returns:
            the value of next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node attribute.
        """
        
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList.

    Attributes:
        head: the head of the list
    """

    def __init__(self):
        """__init__ the constructor of the class.
        """

        self.head = None

    def __str__(self):
        """__str__ this magic method
        prints all nodes at once

        Returns:
            a string with all nodes
        """

        all_nodes = ""
        node = self.head
        while node:
            all_node += "{}\n".format(str(node.data))
            node = node.next_node
        return all_nodes[:-1]

    def sorted_insert(self, value):
        """This method inserts a new Node
        into the correct sorted position
        in the list (increasing order)

        Args:
            value: the node to insert
        """

        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        node = self.head
        
        while node.next_node and node.next_node.data < value:
            node = node.next_node

        if node.next_node:
            new_node.next_node = node.next_node

        node.next_node = new_node
