import java.util.Random;

class Node {
    int ts;
    int value;
    int priority;
    Node left;
    Node right;
    Node parent;

    public Node(int ts, int value) {
        this.ts = ts;
        this.value = value;
        this.priority = (int) Math.floor(new Random().nextFloat() * 100000);
        this.left = null;
        this.right = null;
        this.parent = null;
    }
}

class BinarySearchTree {
    Node root;

    public BinarySearchTree() {
        this.root = null;
    }

    public void insert(Node node) {
        Node y = null;
        Node x = this.root;
        while (x != null) {
            y = x;
            if (node.ts < x.ts) {
                x = x.left;
            } else {
                x = x.right;
            }
        }
        node.parent = y;
        if (y == null) {
            this.root = node;
        } else if (node.ts < y.ts) {
            y.left = node;
        } else {
            y.right = node;
        }
    }

    public Node search(int key) {
        Node x = this.root;
        while (x != null && key != x.ts) {
            if (key < x.ts) {
                x = x.left;
            } else {
                x = x.right;
            }
        }
        return x;
    }

    public void inorderPrint(Node root) {
        if (root != null) {
            inorderPrint(root.left);
            System.out.print(root.ts + " ");
            inorderPrint(root.right);
        }
    }

    public void leftRotate(Node x) {
        //TODO
    }

    public void rightRotate(Node y) {
        //TODO
    }

    public int minimum(Node x) {
        while (x.left != null) {
            x = x.left;
        }
        return x.ts;
    }

    public int maximum(Node x) {
        while (x.right != null) {
            x = x.right;
        }
        return x.ts;
    }

    public int successor(Node x) {
        //TODO
        return -1;
    }

    public int predecessor(Node x) {
        //TODO
        return -1;
    }

    public void fixupInsert(Node z) {
        //TODO
    }

    public int searchOrSum(int ts1, int ts2) {
        //TODO
        return -1;
    }

    public int sumValuesBetween(Node node, int ts1, int ts2) {
        //TODO
        return -1;
    }
}

public class Main {

    public static void main(String[] args) {
        // Your code here
    }
}
