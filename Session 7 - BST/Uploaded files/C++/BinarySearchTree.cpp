#include <iostream>
using namespace std;

class Node {
public:
    int key;
    Node* left;
    Node* right;
    Node* parent;

    Node(int item) : key(item), parent(nullptr), left(nullptr), right(nullptr) {}
};

class BinarySearchTree {
    Node* root;

public:
    BinarySearchTree() : root(nullptr) {}

    void insert(Node* z) {
        Node* y = nullptr;
        Node* x = root;

        while (x != nullptr) {
            y = x;
            if (z->key < x->key) {
                x = x->left;
            } else {
                x = x->right;
            }
        }

        z->parent = y;

        if (y == nullptr) {
            root = z; // This happens when our tree was empty
        } else if (z->key < y->key) {
            y->left = z;
        } else {
            y->right = z;
        }
    }

    Node* search(int k) {
        Node* x = root;
        while (x != nullptr && k != x->key) {
            if (k < x->key) {
                x = x->left;
            } else {
                x = x->right;
            }
        }
        return x;
    }

    void inorderPrint() {
        inorderPrint(root);
        std::cout << std::endl;
    }

private:
    void inorderPrint(Node* node) {
        if (node != nullptr) {
            inorderPrint(node->left);
            std::cout << node->key << " ";
            inorderPrint(node->right);
        }
    }
};

int main() {

    BinarySearchTree bst;
    Node* node = new Node(2);
    bst.insert(node);
    Node* node1 = new Node(12);
    bst.insert(node1);
    Node* node2 = new Node(5);
    bst.insert(node2);
    Node* node3 = new Node(9);
    bst.insert(node3);
    Node* node4 = new Node(17);
    bst.insert(node4);
    Node* node5 = new Node(15);
    bst.insert(node5);
    Node* node6 = new Node(13);
    bst.insert(node6);
    Node* node7 = new Node(19);
    bst.insert(node7);
    Node* node8 = new Node(18);
    bst.insert(node8);

    bst.inorderPrint();

    std::cout << "Searching for key 15..." << std::endl;
    Node* reastchResult = bst.search(15);
    if (reastchResult == nullptr){
        std::cout << "Key 15 not found!" << std::endl;
    }else{
        std::cout << "Key 15 found!" << std::endl;
    }

    std::cout << "Searching for key 18..." << std::endl;
    reastchResult = bst.search(18);
    if (reastchResult == nullptr){
        std::cout << "Key 18 not found!" << std::endl;
    }else{
        std::cout << "Key 18 found!" << std::endl;
    }

    std::cout << "Searching for key 3..." << std::endl;
    reastchResult = bst.search(3);
    if (reastchResult == nullptr){
        std::cout << "Key 3 not found!" << std::endl;
    }else{
        std::cout << "Key 3 found!" << std::endl;
    }

    std::cout << "Searching for key 5..." << std::endl;
    reastchResult = bst.search(5);
    if (reastchResult == nullptr){
        std::cout << "Key 5 not found!" << std::endl;
    }else{
        std::cout << "Key 5 found!" << std::endl;
    }

    std::cout << "Searching for key 7..." << std::endl;
    reastchResult = bst.search(7);
    if (reastchResult == nullptr){
        std::cout << "Key 7 not found!" << std::endl;
    }else{
        std::cout << "Key 7 found!" << std::endl;
    }

    return 0;
}