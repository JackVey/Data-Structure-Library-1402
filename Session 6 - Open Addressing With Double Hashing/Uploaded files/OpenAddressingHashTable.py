class OpenAddressHashTable:
    DELETED = object()

    def __init__(self, m):
        self.m = m
        self.T = [None] * m

    def string_to_integer_converter(self, key):
        int_value = 0
        for char in key:
            int_value += ord(char)
        return int_value

    def hash(self, key, i):
        value = self.string_to_integer_converter(key)
        h1 = value % self.m
        h2 = value % 107
        return (h1 + i * h2) % self.m

    def insert(self, key):
        if key is None or key is self.DELETED:
            raise ValueError("Key cannot be null")

        for i in range(self.m):
            index = self.hash(key, i)
            if self.T[index] is None or self.T[index] is self.DELETED:
                self.T[index] = key
                return i

        return -1

    def search(self, key):
        for i in range(self.m):
            index = self.hash(key, i)
            if self.T[index] is None:
                return -1
            if self.T[index] == key:
                return index
        return -1

    def delete(self, index):
        if index < 0 or index >= self.m:
            return False
        else:
            self.T[index] = self.DELETED
            return True

    def print_hash(self, message):
        print("**************")
        print(message)
        for item in self.T:
            print(item)

if __name__ == "__main__":
    open_address_hash_table = OpenAddressHashTable(10)

    # 1
    res = open_address_hash_table.insert("Algorithm")
    open_address_hash_table.print_hash("Inserted string : Algorithm")
    print("Inserted at i =", res)

    # 2
    res = open_address_hash_table.insert("Data Structure")
    open_address_hash_table.print_hash("Inserted string : Data Structure")
    print("Inserted at i =", res)

    # 3
    res = open_address_hash_table.insert("Hello")
    open_address_hash_table.print_hash("Inserted string : Hello")
    print("Inserted at i =", res)

    # 4
    res = open_address_hash_table.insert("mhtiroglA")
    open_address_hash_table.print_hash("Inserted string : mhtiroglA")
    print("Inserted at i =", res)

    # 5
    index = open_address_hash_table.search("Algorithm")
    result = open_address_hash_table.delete(index)
    open_address_hash_table.print_hash("Deleted string : Algorithm")
    print("Result is", result)

    # 6
    print("UNSUCCESSFUL DELETION BECAUSE THIS KEY DOES NOT EXIST IN OUR HASH TABLE")
    index = open_address_hash_table.search("No")
    result = open_address_hash_table.delete(index)
    open_address_hash_table.print_hash("Deleted string : No")

    # 7
    print("UNSUCCESSFUL SEARCH BECAUSE THIS KEY DOES NOT EXIST IN OUR HASH TABLE")
    res = open_address_hash_table.search("Yes")
    open_address_hash_table.print_hash("Searched string : Yes")
    print("Search result is at", res)

    # 8
    res = open_address_hash_table.search("Data Structure")
    open_address_hash_table.print_hash("Searched string : Data Structure")
    print("Search result is at", res)

    # 9
    res = open_address_hash_table.insert("olleH")
    open_address_hash_table.print_hash("Inserted : olleH")
    print("Inserted at i =", res)
