class Node{
    int key;
    Node prev;
    Node next;
    Node(int value){
        prev = null;
        next = null;
        key = value;
    }
}

class DoublyLinkedList {
    Node head = null;
    Node tail = null;

    void insertBefore(Node y, Node x){
       // TODO
    }

    void insertTail(Node x){
        if (this.tail == null){
            this.head = x;
            this.tail = x;
        }else {
            this.tail.next = x;
            x.prev = this.tail;
            this.tail = x;
        }
    }

    void insertKeepSorted(Node x){
        Node p = this.head;
        while (p != null && p.key < x.key){
            p = p.next;
        }
        if (p == null){
            insertTail(x);
        }else {
            insertBefore(p, x);
        }
    }


    Node search(int value){
        Node node = head;
        while (node != null){
            if (node.key == value){
                break;
            }
            node = node.next;
        }
        return node;
    }

    void delete(Node node) {
        if (head == null || node == null) {
            return;
        }

        if (head == node) {
            head = node.next;
        }

        if (tail == node){
            tail = node.prev;

        }

        if (node.next != null) {
            node.next.prev = node.prev;
        }

        if (node.prev != null) {
            node.prev.next = node.next;
        }

        return;
    }
}

public class Main{
    public static void main(String[] args) {
       // TODO
    }
}