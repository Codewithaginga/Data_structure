#  custom link list 

class Node:

    def __init__(self, data=None):

        self.data = data

        self.next = None


class Linked:

    def __init__(self):

        self.head = None

    def show(self):

        node = self.head

        while node is not None:
            print(node.data)
            node = node.next

    def add(self, new):

        new_node = Node(new) # creating new instance

        new_node.next = self.head
        self.head = new_node



link = Linked()

elem = Node('Aginga')
link.head = elem

elem1 = Node('Edna')

link.head.next = elem1

link.show()

link.add('certified')
link.show()





    