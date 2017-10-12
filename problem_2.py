# problem 2: Flatten a doubly linked list with children


class Node(object):

    def __init__(self, element, next_node, previous_node, child_node):
        """create a new node
        :param element: the element value
        :param next_node: the next linked node
        :return:
        """
        self.element = element
        self.next_node = next_node
        self.previous_node = previous_node
        self.child_node = child_node


head_node = Node(5, Node(33, Node(17, Node(2, None, None, Node(2, None, None, Node(12, None, None, None))), None, None),
                         None, None), None, Node(6, Node(25, None, None, Node(8, None, None, None)), None, None))

