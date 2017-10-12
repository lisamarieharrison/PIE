# Graph solution to Kevin Bacon problem

from multiprocessing import Queue

class Node(object):

    def __init__(self, name, bacon_number=-1, linked_actors={}):
        self.name = name
        self.bacon_number = bacon_number
        self.linked_actors = linked_actors

    def add_link(self, actor_node):
        self.linked_actors.add(actor_node)


def find_bacon(node, actor):

    actor_q = Queue()
    actor_q.put(node)

    while actor_q.qsize() > 0:

        current_node = actor_q.get()

        if current_node.name == actor:  # if it's the node we are interested in then return bacon number
            return current_node.bacon_number
        for link in current_node.linked_actors:
            if link is not None and link.bacon_number == -1:
                link.bacon_number = current_node.bacon_number + 1
                actor_q.put(link)

    return False




bacon = Node(name='Bacon', bacon_number=0, linked_actors={Node('Damon', linked_actors={Node('Kidman',
                linked_actors={Node('Weaving')}), Node('Jackman')}), Node('Willis')})



print(find_bacon(bacon, 'Jackman'))
