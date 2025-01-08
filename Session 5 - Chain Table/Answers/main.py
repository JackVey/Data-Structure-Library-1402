import time

class Node:
    def __init__(self, k, val=None):
        self.k = k
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return f"{self.k}:{self.val}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_tail(self, x):
        if self.tail is None:
            self.head = x
            self.tail = x
        else:
            self.tail.next = x
            x.prev = self.tail
            self.tail = x

    def search(self, value):
        node = self.head
        while node is not None:
            if node.k == value:
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


class HashTable:
    def __init__(self, size) -> None:
        self.size = size // 10
        self.table = [DoublyLinkedList() for _ in range(self.size)]

    def get_hash(self, k):
        if not k.isdigit():
            return sum([ord(c) for c in k]) % self.size
        else:
            return int(k) % self.size

    def insert(self, node: Node):
        chain = self.table[self.get_hash(node.k)]
        if not chain.search(node.k):
            chain.insert_tail(node)

    def search(self, k):
        chain = self.table[self.get_hash(k)]
        return chain.search(k)

    def delete(self, node: Node):
        chain = self.table[self.get_hash(node.k)]
        chain.delete(node)


def Read_time(name):
    av_t = 0
    for i in range(0, 4):
        start_time = time.time()
        with open(name, 'r') as f:
            strings = f.read().splitlines()
            strings[0] = strings[0] + 'a'
        t = time.time() - start_time

        av_t += t
    return av_t / 4


# ----------- اجرای کد با ساختار جدید -----------

a = Read_time("db.txt")
print(f"read for db.txt: {a} seconds")

a = Read_time("query1.txt")
print(f"read for query1.txt: {a} seconds")

a = Read_time("query2.txt")
print(f"read for query2.txt: {a} seconds")

# ------------ Reading from db.txt and insertion to list ------------

T = HashTable(100000)

db_lines = None

start_time = time.time()
with open("db.txt", "r") as file:
    db_lines = file.readlines()

for line in db_lines:
    line = line.split()
    T.insert(Node(line[0], line[1]))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed Time: {elapsed_time} seconds to read db.txt and insert all lines to the list")

# ------------ Reading from query1.txt & and searching through the list ------------

q1_lines = None

start_time = time.time()
with open("query1.txt", "r") as file:
    q1_lines = file.readlines()

for line in q1_lines:
    node = T.search(line.strip())

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed Time: {elapsed_time} seconds to read query1.txt and search all the lines from the list")

# ------------ Reading from query3.txt & and searching through the list ------------

q3_lines = None

start_time = time.time()
with open("query2.txt", "r") as file:
    q3_lines = file.readlines()

for line in q3_lines:
    node = T.search(line.strip())

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed Time: {elapsed_time} seconds to read query2.txt and search all the lines from the list")

# ------------ Reading from query1.txt & and deleting from the list ------------

q1_lines = None

start_time = time.time()
with open("query1.txt", "r") as file:
    q1_lines = file.readlines()

for line in q1_lines:
    node = T.search(line.strip())
    if node:
        T.delete(node)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed Time: {elapsed_time} seconds to read query1.txt and delete all the lines from the list")
