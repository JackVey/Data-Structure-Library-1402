class Interval:
    def __init__(self, low, high):
        self.low = low
        self.high = high

class Node:
    def __init__(self, interval):
        self.i = interval
        self.max = interval.high
        self.left = None
        self.right = None

def new_node(interval):
    return Node(interval)

def insert(root, interval):
    # TODO
    pass

def do_overlap(i1, i2):
    return i1.low <= i2.high and i2.low <= i1.high

def overlap_search(root, interval):
    # TODO
    pass

def left_most_search(root, interval):
    # TODO
    pass

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def successor(root, interval):
    current = None
    successor = None

    while root is not None:
        if root.i.low > interval.low:
            successor = root
            root = root.left
        elif root.i.low < interval.low:
            root = root.right
        else:
            if root.right is not None:
                successor = find_min(root.right)
            break

    return successor
