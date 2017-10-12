from itertools import izip_longest

class Node(object):

    def __init__(self, element, previous_node=None, next_node=None):
        self.element = element
        self.previous_node = previous_node
        self.next_node = next_node

def traverse(node, backwards=False):
    if backwards:
        head = node.previous_node
        current_node = head.previous_node
    else:
        head = node
        current_node = head.next_node

    ls = [head.element]
    while current_node is not head and current_node is not None:
        ls.append(current_node.element)
        if backwards:
            current_node = current_node.previous_node
        else:
            current_node = current_node.next_node
    return ls




# node0 = Node(0)
# node1 = Node(1, node0, None)
# node0.next_node = node1
# node2 = Node(2, node1, node0)
# node1.next_node = node2
# node0.previous_node = node2

#     4
#  2     5
# 1 3

# tree = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
tree = Node(4, Node(2, Node(1), Node(3)), Node(5))

# 1 2 3 4 5 6 7


def tree_to_list(node):

    if node.next_node is None and node.previous_node is None:
        node.next_node = node
        node.previous_node = node
        return node
    else:
        if node.previous_node is not None and node.next_node is None:
            left_result = tree_to_list(node.previous_node)
            node.next_node = node
            node.previous_node = left_result
            node.next_node.next_node = node
            node.next_node.previous_node = node

    return node

#    3
#  2
# 1

head = tree_to_list(Node(3, Node(2, Node(1))))


def insert_list(ls1, ls2):

    l2_current = ls2
    l2_tail = None
    while l2_current is not None:
        l2_tail = l2_current
        l2_current = l2_current.next_node

    l1_current = ls1
    while l1_current is not None:
        if l1_current.element < ls2.element and l1_current.next_node.element > l2_tail.element:
            temp = l1_current.next_node
            l1_current.next_node = ls2
            ls2.previous_node = l1_current.next_node
            l2_tail.next_node = temp
            temp.previous_node = l2_tail
            return ls1
        l1_current = l1_current.next_node

    return None


node0 = Node(0)
node1 = Node(1, node0, None)
node0.next_node = node1
node2 = Node(5, node1, None)
node1.next_node = node2

list0 = Node(2)
list1 = Node(3, list0, None)
list0.next_node = list1
list2 = Node(4, list1, None)
list1.next_node = list2


tree = Node(10, Node(11, Node(12)), Node(4, Node(14)))


def print_tree(t):

    if t.next_node is None and t.previous_node is None:
        return t.element

    else:
        if t.previous_node is not None:
            left = print_tree(t.previous_node)
        else:
            left = ' '
        if t.next_node is not None:
            right = print_tree(t.next_node)
        else:
            right = ' '

        # if there are linebreaks
        n_loc = str(left).find('\n')
        n_loc_right = str(right).find('\n')
        print repr(str(left)), repr(str(right))
        if n_loc != -1: # if on left
            children = str(left)[:n_loc] + ' ' + str(right) + str(left)[n_loc:]
        elif n_loc_right != -1: # if on right
            children = str(left) + ' ' + str(right)
        else:
            children = str(left) + ' ' + str(right)

        return ' '*(len(children)/3) + str(t.element) + '\n' + children


print print_tree(tree)



