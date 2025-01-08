import time

primes = [100193, 103067, 103993]


class record:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f'{self.name} {self.number}'

class OpenAddressHashTable:
    DELETED = None

    def __init__(self, m):
        self.m = m
        self.T = [None] * m

    def hash(self, key, i):
        value1 = hash(key)
        h1 = value1 % self.m
        value2 = 1 + h1 % (self.m - 1)

        h2 = value2 % 534 + 1
        return (h1 + i * h2) % self.m

    def insert(self, key):
        if key is None or key == self.DELETED:
            raise ValueError("Key cannot be null")

        for i in range(self.m):
            index = self.hash(key.name, i)
            if self.T[index] is None or self.T[index] == self.DELETED:
                self.T[index] = key
                return index

        return -1

    def search(self, key):
        for i in range(self.m):
            index = self.hash(key, i)
            if self.T[index] is None:
                return None
            if self.T[index].name == key:
                return self.T[index]
        print("Key not found ")
        return None


for m in primes:
    DB = OpenAddressHashTable(m)
    print('the Open address hash table using m:' + str(m))
    try:
        with open('db.txt', 'r') as input_file:
            i = 0
            start = time.time()
            for line in input_file:
                string, num = line.split()
                rec = record(string, num)
                DB.insert(rec)
                i += 1
            end = time.time()
            print(f"Time to insert to the list: {end - start}s")
    except FileNotFoundError:
        print("Failed to open the file.")

    try:
        with open('query_string.txt', 'r') as query_file:
            start = time.time()
            for line in query_file:
                string = line.strip()
                name, num = string.split(' ')
                DB.search(name)
            end = time.time()
            print(f"Time to search string the list: {end - start}s")
    except FileNotFoundError:
        print("Failed to open the file.")

    try:
        with open('Not_db_string.txt', 'r') as query_file:
            start = time.time()
            for line in query_file:
                string = line
                DB.search(string)
            end = time.time()
            print(f"Time to search not in the db numbers in the list: {end - start}s")
    except FileNotFoundError:
        print("Failed to open the file.")
