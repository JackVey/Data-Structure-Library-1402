#include <iostream>
#include <string>
#include <vector>

class OpenAddressHashTable {
private:
    int m;
    static const std::string DELETED;
    std::vector<std::string> T;

    int stringToIntegerConverter(const std::string& key) const {
        int intValue = 0;
        for (char ch : key) {
            intValue += static_cast<int>(ch);
        }
        return intValue;
    }

    int hash(const std::string& key, int i) const {
        int value = stringToIntegerConverter(key);
        int h1 = value % m;
        int h2 = value % 107;
        return (h1 + i * h2) % m;
    }

public:
    OpenAddressHashTable(int m) : m(m), T(m, "") {}

    int insert(const std::string& key) {
        if (key.empty() || key == DELETED) {
            throw std::invalid_argument("Key cannot be empty or DELETED");
        }

        for (int i = 0; i < m; i++) {
            int index = hash(key, i);
            if (T[index].empty() || T[index] == DELETED) {
                T[index] = key;
                return i;
            }
        }
        return -1; // Table is full
    }

    int search(const std::string& key) const {
        for (int i = 0; i < m; i++) {
            int index = hash(key, i);
            if (T[index].empty()) {
                return -1; // Key not found
            }
            if (T[index] == key) {
                return index;
            }
        }
        return -1; // Key not found
    }

    bool deleteKey(int index) {
        if (index < 0 || index >= m) {
            return false;
        } else {
            T[index] = DELETED;
            return true;
        }
    }

    void printHash(const std::string& message) const {
        std::cout << "**************\n";
        std::cout << message << std::endl;
        for (const auto& item : T) {
            std::cout << item << std::endl;
        }
    }
};

// Define the DELETED constant
const std::string OpenAddressHashTable::DELETED = std::string();

int main() {
    OpenAddressHashTable openAddressHashTable(10);

    int res;

    // 1
    res = openAddressHashTable.insert("Algorithm");
    openAddressHashTable.printHash("Inserted string: Algorithm");
    std::cout << "Inserted at i = " << res << std::endl;

    // 2
    res = openAddressHashTable.insert("Data Structure");
    openAddressHashTable.printHash("Inserted string: Data Structure");
    std::cout << "Inserted at i = " << res << std::endl;

    // 3
    res = openAddressHashTable.insert("Hello");
    openAddressHashTable.printHash("Inserted string: Hello");
    std::cout << "Inserted at i = " << res << std::endl;

    // 4
    res = openAddressHashTable.insert("mhtiroglA");
    openAddressHashTable.printHash("Inserted string: mhtiroglA");
    std::cout << "Inserted at i = " << res << std::endl;

    // 5
    int index = openAddressHashTable.search("Algorithm");
    bool result = openAddressHashTable.deleteKey(index);
    openAddressHashTable.printHash("Deleted string: Algorithm");
    std::cout << "Result is " << std::boolalpha << result << std::endl;

    // 6
    std::cout << "UNSUCCESSFUL DELETION BECAUSE THIS KEY DOES NOT EXIST IN OUR HASH TABLE" << std::endl;
    index = openAddressHashTable.search("No");
    result = openAddressHashTable.deleteKey(index);
    openAddressHashTable.printHash("Deleted string: No");

    // 7
    std::cout << "UNSUCCESSFUL SEARCH BECAUSE THIS KEY DOES NOT EXIST IN OUR HASH TABLE" << std::endl;
    res = openAddressHashTable.search("Yes");
    openAddressHashTable.printHash("Searched string: Yes");
    std::cout << "Search result is at " << res << std::endl;

    // 8
    res = openAddressHashTable.search("Data Structure");
    openAddressHashTable.printHash("Searched string: Data Structure");
    std::cout << "Search result is at " << res << std::endl;

    // 9
    res = openAddressHashTable.insert("olleH");
    openAddressHashTable.printHash("Inserted: olleH");
    std::cout << "Inserted at i = " << res << std::endl;

    return 0;
}
