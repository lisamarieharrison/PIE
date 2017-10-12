# Problem 4: Find the height of a given tree


class Node(object):

    def __init__(self, element, left_child=None, right_child=None):
        """create a new node
        :param element: the element value
        :param left_child: the left child of a node
        :param right_child: the right child of a node
        """
        self.element = element
        self.left_child = left_child
        self.right_child = right_child


    def height(self):
        """
        return the height of a tree
        :param node: node root
        :return: int tree height
        """
        left_height = self.left_child.height() if self.left_child is not None else 0
        right_height = self.right_child.height() if self.right_child is not None else 0
        return 1 + max(left_height, right_height)

    def common_ancestor(self, node1, node2):
        current_node = self
        while current_node is not None:
            if node1.element <= current_node.element <= node2.element:
                return current_node.element
            if node1.element < current_node.element:
                current_node = current_node.left_child
            else:
                current_node.element = current_node.right_child
        return None


def tree_size(node, size=0):

    if node is None:
        return 0
    else:
        return tree_size(node.left_child, size) + tree_size(node.right_child, size) + 1


def traversal(node):
    """
    traverse a tree using preorder traversal with recursion
    :param node: node root
    """
    if node is None:
        return None
    else:
        print node.element
        traversal(node.left_child)
        traversal(node.right_child)


def traversal_norec(node):
    """
    traverse a tree using preorder traversal without recursion
    :param node: node root
    """
    node_stack = []
    node_stack.append(node)
    while len(node_stack) != 0:
        current_node = node_stack.pop()
        print(current_node.element)
        if current_node.right_child is not None:
            node_stack.append(current_node.right_child)
        if current_node.left_child is not None:
            node_stack.append(current_node.left_child)


def to_array(node, array=[]):
    if node is None:
        return array
    else:
        array.append(node)
        to_array(node.left_child, array)
        to_array(node.right_child, array)
        return array


def heapify(node):
    """
    convert a BST into a min heap
    :param node: the root of the BST
    :return: the new heap root (min value)
    """

    node_array = to_array(node)  # put tree into array
    node_array.sort(key=lambda x: x.element)  # sort by element

    # assign new children
    for i, node in enumerate(node_array):
        left_pos = 2*i + 1
        right_pos = left_pos + 1
        if left_pos < len(node_array):
            node.left_child = node_array[left_pos]
        else:
            node.left_child = None
        if right_pos < len(node_array):
            node.right_child = node_array[right_pos]
        else:
            node.right_child = None

    return node_array[0]


def rotate_right(node):

    new_root = node.left_child
    node.left_child = new_root.right_child
    new_root.right_child = node

    return new_root


#test_tree = Node(20, left_child=Node(8, Node(4), Node(12, Node(10), Node(14))), right_child=Node(22))


test_tree = Node(6, Node(4, Node(2, Node(1), Node(3)), Node(5)), Node(7))

new_tree = rotate_right(test_tree)

traversal(new_tree)