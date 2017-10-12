# power


def power(num, pwr):
    if pwr == 0:
        return 1

    if pwr == 1:
        return num
    else:
        return num * power(num, pwr - 1)


# greatest common divisor

# int gcd(int m, int n) {
#    if ((m % n) == 0)
#       return n;
#    else
#       return gcd(n, m % n);
# }


def greatest_div(num1, num2, acc=0):
    div = min(num1, num2)

    if (num1 + acc) % div == 0 and num2 % div == 0:
        return div
    else:
        return greatest_div(div - 1, max(num1, num2), acc + 1)


# find largest element in tree with 0-n children

class Node(object):
    def __init__(self, element, children):
        self.element = element
        self.children = children

    def __str__(self):
        return "[Node=" + str(self.element) + "]"


tree = Node(1, [Node(2, None), Node(5, None), Node(3, [Node(4, None), Node(6, None)])])


#     1
# 2   5   3
#        4 6


def largest_element(t):
    if t.children is None:
        return t.element
    else:
        current_max = t.element
        for child in t.children:
            current_max = max(current_max, largest_element(child))
        return current_max


class Node(object):
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node


def traverse(list):
    current_node = list
    out_list = []
    while current_node is not None:
        out_list.append(current_node.element)
        current_node = current_node.next_node
    return out_list


def insert_list(list_1, list_2):
    list2_current = list2
    list2_tail = None
    while list2_current is not None:
        list2_tail = list2_current
        list2_current = list2_current.next_node

    current_node = list1
    while current_node is not None:

        if current_node.element < list2.element and current_node.next_node.element > list2_tail.element:
            temp = current_node.next_node
            current_node.next_node = list2
            list2_tail.next_node = temp
            return list_1

        current_node = current_node.next_node

    return None


list1 = Node(0, Node(1, Node(2, Node(6, Node(7)))))
list2 = Node(3, Node(4, Node(5)))

full_list = insert_list(list1, list2)

print traverse(full_list)
