class Node:
    def __init__(self, value):
        self.key = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_before(self, y, x):
        pass
        # TODO

    def insert_tail(self, x):
        if self.tail is None:
            self.head = x
            self.tail = x
        else:
            self.tail.next = x
            x.prev = self.tail
            self.tail = x

    def insert_keep_sorted(self, x):
        p = self.head
        while p is not None and p.key < x.key:
            p = p.next

        if p is None:
            self.insert_tail(x)
        else:
            self.insert_before(p, x)

    def search(self, value):
        node = self.head
        while node is not None:
            if node.key == value:
                return node
            node = node.next
        return None

    def delete(self, node):
        if self.head is None or node is None:
            return

        if self.head == node:
            self.head = node.next

        if self.tail == node:
            self.tail = node.prev

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

# Example usage
if __name__ == "__main__":
    pass
    # TODO
