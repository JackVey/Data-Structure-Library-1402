import java.util.*;

class Interval {
    double low, high;

    public Interval(double low, double high) {
        this.low = low;
        this.high = high;
    }
}

class Node {
    Interval i;
    double max;
    Node left, right;

    public Node(Interval i) {
        this.i = i;
        this.max = i.high;
        this.left = null;
        this.right = null;
    }
}

class IntervalTree {

    public Node newNode(Interval i) {
        return new Node(i);
    }

    public Node insert(Node root, Interval i) {
        // TODO: Implement the insert function
        return root;
    }

    public boolean doOverlap(Interval i1, Interval i2) {
        return i1.low <= i2.high && i2.low <= i1.high;
    }

    public Node overlapSearch(Node root, Interval i) {
        // TODO: Implement the overlapSearch function
        return null;
    }

    public Node leftMostSearch(Node root, Interval i) {
        // TODO: Implement the leftMostSearch function
        return null;
    }

    public Node findMin(Node node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }

    public Node successor(Node root, Interval i) {
        Node current = null;
        Node successor = null;

        while (root != null) {
            if (root.i.low > i.low) {
                successor = root;
                root = root.left;
            } else if (root.i.low < i.low) {
                root = root.right;
            } else {
                if (root.right != null) {
                    successor = findMin(root.right);
                }
                break;
            }
        }

        return successor;
    }
}
