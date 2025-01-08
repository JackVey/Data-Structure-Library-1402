import random
import time


class Node:
    def __init__(self, interval):
        self.interval = interval
        self.priority = random.randint(1, 1000000)
        self.max = interval[1]
        self.left = None
        self.right = None


class TreapIntervalTree:
    def __init__(self):
        self.root = None

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.update_max(node)
        self.update_max(new_root)
        return new_root

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.update_max(node)
        self.update_max(new_root)
        return new_root

    def update_max(self, node):
        if not node:
            return
        node.max = max(
            node.interval[1],
            (node.left.max if node.left else float('-inf')),
            (node.right.max if node.right else float('-inf'))
        )

    def insert(self, root, interval):
        if not root:
            return Node(interval)

        if interval[0] < root.interval[0]:
            root.left = self.insert(root.left, interval)
            if root.left.priority > root.priority:
                root = self.rotate_right(root)
        else:
            root.right = self.insert(root.right, interval)
            if root.right.priority > root.priority:
                root = self.rotate_left(root)

        self.update_max(root)
        return root

    def overlap(self, interval1, interval2):
        return interval1[0] <= interval2[1] and interval2[0] <= interval1[1]

    def count_overlaps(self, root, interval):
        if not root:
            return 0

        count = 0
        if self.overlap(root.interval, interval):
            count += 1

        if root.left and root.left.max >= interval[0]:
            count += self.count_overlaps(root.left, interval)

        count += self.count_overlaps(root.right, interval)

        return count

    def search_overlap(self, root, interval):
        if not root:
            return None

        if self.overlap(root.interval, interval):
            return root.interval

        if root.left and root.left.max >= interval[0]:
            return self.search_overlap(root.left, interval)

        return self.search_overlap(root.right, interval)

    def add_interval(self, interval):
        self.root = self.insert(self.root, interval)


    def find_overlap(self, interval):
        return self.search_overlap(self.root, interval)

    def left_most_search(self, root, interval):
        result = None
        while root:
            if self.overlap(root.interval, interval):
                result = root.interval
                root = root.left
            elif root.left and root.left.max >= interval[0]:
                root = root.left
            else:
                root = root.right
        return result

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def successor(self, root, interval):
        current = None
        successor = None

        while root is not None:
            if root.interval[0] > interval[0]:
                successor = root
                root = root.left
            elif root.interval[0] < interval[0]:
                root = root.right
            else:
                if root.right is not None:
                    successor = self.find_min(root.right)
                break

        return successor

    def load_intervals_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                a, b = map(int, line.strip().split())
                self.add_interval((a, b))


if __name__ == '__main__':
    db1_tree = TreapIntervalTree()
    db2_tree = TreapIntervalTree()
    db3_tree = TreapIntervalTree()

    start = time.time()
    db1_tree.load_intervals_from_file("DB1.txt")
    end = time.time()
    print(f"Time for insert DB1 : {end - start}")

    start = time.time()
    db2_tree.load_intervals_from_file("DB2.txt")
    end = time.time()
    print(f"Time for insert DB2 : {end - start}")

    start = time.time()
    db3_tree.load_intervals_from_file("DB3.txt")
    end = time.time()
    print(f"Time for insert DB2 : {end - start}")

    query_files = ["Query1.txt", "Query2.txt", "Query3.txt"]
    db_trees = [db1_tree, db2_tree, db3_tree]

    for query_file, db_tree in zip(query_files, db_trees):
        print(f"Processing {query_file}:")
        total_overlaps = 0
        overlap_counts = []
        with open(query_file, "r") as file:
            start = time.time()
            for line in file:
                a, b = map(int, line.strip().split())
                count = db_tree.count_overlaps(db_tree.root, (a, b))
                overlap_counts.append(count)
            end = time.time()
        print(f"Total overlaps for {query_file}: {sum(overlap_counts)}")
        print(f"Smallest number of overlaps: {min(overlap_counts)}")
        print(f"Largest number of overlaps: {max(overlap_counts)}")
        print(f"Average number of overlaps: {sum(overlap_counts) / len(overlap_counts):.2f}")
        print(f"Time for searching overlaps from {query_file} in tree: {end - start}")