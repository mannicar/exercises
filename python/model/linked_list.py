class LinkedList(object):

    class Node(object):
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = None
        self.length = 0

    def len(self):
        return self.length

    def add(self, node):
        n = self.head
        if n is None:
            self.head = node
        else:
            while n.next is not None:
                n = n.next
            n.next = node
        self.length += 1

    def get(self, index):
        if index <= self.length - 1:
            n = self.head
            while index > 0:
                n = n.next
                index -= 1
            return n
        return self.get(index - self.length)

    def delete(self, index):
        if index == 0:
            self.head = self.head.next
        elif index <= self.length - 1:
            prev_node = self.get(index - 1)
            child_node = prev_node.next.next if index <= self.length - 2 else None
            prev_node.next = child_node
        self.length -= 1
