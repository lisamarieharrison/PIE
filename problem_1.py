# Problem 1: Stack implementation using singly linked list
# Problem 2: Add features to the stack including delete at index and add after index
# Problem 3: Add function to return mth from end elements

import unittest


class Node(object):

    def __init__(self, element, next_node):
        """create a new node
        :param element: the element value
        :param next_node: the next linked node
        :return:
        """
        self.element = element
        self.next_node = next_node


class Stack(object):

    def __init__(self, head):
        """create a new stack with the given element as head
        :param head: the element to become the head
        """
        self.head = Node(element=head, next_node=None)
        self.tail = Node(element=head, next_node=None)

    def pop(self):
        """remove the first element
        :return old head
        """
        old_head = self.head
        self.head = old_head.next_node
        return old_head

    def push(self, new_element):
        """add a new element to the front
        :param new_element: the value to add to the stack
        :return: the new head
        """
        old_head = self.head
        self.head = Node(element=new_element, next_node=old_head)
        return self.head

    def print_stack(self):
        """print all elements in stack"""
        current_element = self.head
        while current_element is not None:
            print(current_element.element)
            current_element = current_element.next_node
        print("Finished printing stack")

    def return_stack(self):
        """
        returns the full stack as array for unit testing
        :return: array of all values in stack
        """
        current_element = self.head
        stack_array = []
        while current_element is not None:
            stack_array.append(current_element.element)
            current_element = current_element.next_node
        return  stack_array

    def delete(self, element_index):
        """ delete the node at element_index
        :param element_index: int element index to delete
        :return: deleted node
        """
        prev_element = self.head
        for i in range(1, element_index):
            prev_element = prev_element.next_node
        deleted_element = prev_element.next_node
        # if the tail is to be removed we need to make a new tail
        if deleted_element.next_node is None:
            prev_element.next_node = None
            self.tail = prev_element
        else:
            prev_element.next_node = Node(deleted_element.next_nodee.element, deleted_element.next_node.next_node)
        return deleted_element

    def insert_after(self, element_index, new_element):
        """ insert a new node after the given index
        :param element_index: int index to insert parameter after
        :param new_element: element value to insert
        :return: the new node
        """
        prev_element = self.head
        for i in range(0, element_index):
            prev_element = prev_element.next_node
        # if the new item is inserted at the end we need to make a new tail
        if prev_element.next_node is None:
            new_node = Node(new_element, None)
            prev_element.next_node = new_node
            self.tail = new_node
        else:
            new_node = Node(new_element, prev_element.next_node)
            prev_element.next_node = new_node
        return new_node

    def list_length(self):
        """
        counts how many elements are in the list
        :return: int number of elements
        """
        length = 0
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next_node
        return length

    def m_to_last(self, m):
        current_node = self.head
        saved_array = [None]*(m+1)
        while current_node is not None:
            saved_array.append(current_node.element)
            saved_array.pop(0)
            current_node = current_node.next_node
        if any([x is None for x in saved_array]):
            raise ValueError("List is longer than "+str(m))
        return saved_array

    def __del__(self):
        """ delete the stack"""


class TestStack(unittest.TestCase):

    def test_push(self):
        test_stack = Stack(head=1)
        test_stack.push(new_element=2)
        out = test_stack.return_stack()
        self.assertEqual(out, [2, 1])

    def test_pop(self):
        test_stack = Stack(head=1)
        test_stack.push(new_element=2)
        test_stack.pop()
        out = test_stack.return_stack()
        self.assertEqual(out, [1])

    def test_delete(self):
        test_stack = Stack(head=1)
        test_stack.push(new_element=2)
        test_stack.push(new_element=3)
        test_stack.push(new_element=4)
        test_stack.delete(2)
        out = test_stack.return_stack()
        self.assertEqual(out, [4, 3, 1])

    def test_delete(self):
        test_stack = Stack(head=1)
        test_stack.push(new_element=3)
        test_stack.push(new_element=4)
        test_stack.insert_after(1, 2)
        out = test_stack.return_stack()
        self.assertEqual(out, [4, 3, 2, 1])

    def test_delete_tail(self):
        test_stack = Stack(head=1)
        for i in range(2, 5):
            test_stack.push(new_element=i)
        test_stack.delete(3)
        out = test_stack.return_stack()
        self.assertEqual(out, [4, 3, 2])
        self.assertEqual(test_stack.tail.element, 2)

    def test_insert_tail(self):
        test_stack = Stack(head=2)
        for i in range(3, 5):
            test_stack.push(new_element=i)
        test_stack.insert_after(2, new_element=1)
        out = test_stack.return_stack()
        self.assertEqual(out, [4, 3, 2, 1])
        self.assertEqual(test_stack.tail.element, 1)

    def test_list_length(self):
        test_stack = Stack(head=1)
        for i in range(2, 5):
            test_stack.push(new_element=i)
        length = test_stack.list_length()
        self.assertEqual(length, 4)

    def test_m_to_last(self):
        test_stack = Stack(head=1)
        for i in range(2, 11):
            test_stack.push(new_element=i)
        out = test_stack.m_to_last(4)
        self.assertEqual(out, [5, 4, 3, 2, 1])
        out = test_stack.m_to_last(0)
        self.assertEqual(out, [1])

    def test_m_to_last_long(self):
        test_stack = Stack(head=1)
        for i in range(2, 11):
            test_stack.push(new_element=i)
        self.assertRaises(ValueError, test_stack.m_to_last, 20)

unittest.main()