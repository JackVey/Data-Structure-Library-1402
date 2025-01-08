public class BinarySearchTree {
    Node root;
    public BinarySearchTree(){
        root = null;
    }

    public void insert(Node z){
        Node y = null;
        Node x = this.root;
        while (x != null){
            y = x;
            if (z.key < x.key){
                x = x.left;
            }else {
                x = x.right;
            }
        }
        z.parent = y;
        if (y == null){
            this.root = z; // This happens when our tree was empty
        }else if (z.key < y.key){
            y.left = z;
        }else {
            y.right = z;
        }
    }

    public Node search(int k){
        Node x = this.root;
        while (x != null && k != x.key){
            if (k < x.key){
                x = x.left;
            }else {
                x = x.right;
            }
        }
        return x;
    }

    void inorderPrint(Node root)
    {
        if (root != null) {
            inorderPrint(root.left);
            System.out.print(root.key + " ");
            inorderPrint(root.right);
        }
    }
}

class Node {
    int key;
    Node left;
    Node right;
    Node parent;

    public Node(int item)
    {
        key = item;
        parent = left = right = null;

    }
}

class Main{
    public static void main(String[] args) {
        BinarySearchTree BST = new BinarySearchTree();
        Node node = new Node(2);
        Node node1 = new Node(12);
        Node node2 = new Node(5);
        Node node3 = new Node(9);
        Node node4 = new Node(17);
        Node node5 = new Node(15);
        Node node6 = new Node(13);
        Node node7 = new Node(19);
        Node node8 = new Node(18);
        BST.insert(node);
        BST.insert(node1);
        BST.insert(node2);
        BST.insert(node3);
        BST.insert(node4);
        BST.insert(node5);
        BST.insert(node6);
        BST.insert(node7);
        BST.insert(node8);
        BST.inorderPrint(BST.root);
        System.out.println();

        System.out.println("Searching for key 15...");
        Node searchResult = BST.search(15);
        if (searchResult == null){
            System.out.println("Key 15 not found!");
        }else {
            System.out.println("Key 15 found!");
        }
        System.out.println("Searching for key 18...");
        searchResult = BST.search(18);
        if (searchResult == null){
            System.out.println("Key 18 not found!");
        }else {
            System.out.println("Key 18 found!");
        }
        System.out.println("Searching for key 3...");
        searchResult = BST.search(3);
        if (searchResult == null){
            System.out.println("Key 3 not found!");
        }else {
            System.out.println("Key 3 found!");
        }

        System.out.println("Searching for key 5...");
        searchResult = BST.search(5);
        if (searchResult == null){
            System.out.println("Key 5 not found!");
        }else {
            System.out.println("Key 5 found!");
        }

        System.out.println("Searching for key 7...");
        searchResult = BST.search(7);
        if (searchResult == null){
            System.out.println("Key 7 not found!");
        }else {
            System.out.println("Key 7 found!");
        }
    }
}