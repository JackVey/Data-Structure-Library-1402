public class OpenAddressHashTable {
    private int m;
    private static final String DELETED = new String();
    private String[] T;

    public OpenAddressHashTable(int m) {
        this.m = m;
        this.T = new String[m];
        // everything in java initialized by null by default
    }

    private int stringToIntegerConvertor(String key){
        int intValue = 0;
        for (int i = 0; i < key.length(); i++){
            intValue += (int)key.charAt(i);
        }
        return intValue;
    }

    private int hash(String key, int i) {
        int value = stringToIntegerConvertor(key);
        int h1 = value % this.m;
        int h2 = value % 107;
        return ((h1 + i * h2) % this.m);
    }

    public int insert(String key) {
        if (key == null || key == DELETED) {
            throw new IllegalArgumentException("Key cannot be null");
        }

        for (int i = 0; i < this.m; i++){
            int index = hash(key, i);
            if (T[index] == null || T[index] == DELETED){
                T[index] = key;
                return i;
            }
        }

        return -1;
    }


    public int search(String key) {
        for (int i = 0; i < this.m; i++){
            int index = hash(key, i);
            if (T[index] == null){
                return -1;
            }
            if (T[index] == key){
                return index;
            }
        }
        return -1;
    }

    public boolean delete(int index ) {
        if (index < 0 || index >= this.m){
            return false;
        }else {
            T[index] = DELETED;
            return true;
        }
    }

    public void printHash(String message){
        System.out.println("**************");
        System.out.println(message);
        for (int i = 0; i < this.m; i++){
            System.out.println(this.T[i]);
        }
    }

    public static void main(String[] args) {
        OpenAddressHashTable openAddressHashTable = new OpenAddressHashTable(10);
        boolean result = false;
        int res;

        //1
        res = openAddressHashTable.insert("Algorithm");
        openAddressHashTable.printHash("Inserted string : Algorithm");
        System.out.println("Inserted at i = " + res);

        //2
        res = openAddressHashTable.insert("Data Structure");
        openAddressHashTable.printHash("Inserted string : Data Structure");
        System.out.println("Inserted at i = " + res);

        //3
        res = openAddressHashTable.insert("Hello");
        openAddressHashTable.printHash("Inserted string : Hello");
        System.out.println("Inserted at i = " + res);

        //4
        res = openAddressHashTable.insert("mhtiroglA");
        openAddressHashTable.printHash("Inserted string : mhtiroglA");
        System.out.println("Inserted at i = " + res);

        //5
        int index = openAddressHashTable.search("Algorithm");
        result = openAddressHashTable.delete(index);
        openAddressHashTable.printHash("Deleted string : Algorithm");
        System.out.println("Result is " + result);

        //6
        System.out.println("UNSUCCESSFUL DELETION BECAUSE THIS KEY DOES NOT EXIST IN OUR HASH TABLE");
        index = openAddressHashTable.search("No");
        result = openAddressHashTable.delete(index);
        openAddressHashTable.printHash("Deleted string : No");

        //7
        System.out.println("UNSUCCESSFUL SEARCH BECAUSE THIS KEY DOES NOT EXIST IN OUR HASH TABLE");
        res = openAddressHashTable.search("Yes");
        openAddressHashTable.printHash("Searched string : Yes");
        System.out.println("Search result is at " + res);

        //8
        res = openAddressHashTable.search("Data Structure");
        openAddressHashTable.printHash("Searched string : Data Structure");
        System.out.println("Search result is at " + res);

        //9
        res = openAddressHashTable.insert("olleH");
        openAddressHashTable.printHash("Inserted : olleH");
        System.out.println("Inserted at i = " + res);
    }
}