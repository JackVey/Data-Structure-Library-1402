#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>

using namespace std;

class Node {
public:
    int ts;
    int value;
    int priority;
    Node* left;
    Node* right;
    Node* parent;

    Node(int ts, int value) {
        this->ts = ts;
        this->value = value;
        this->priority = floor(static_cast<float>(rand()) / RAND_MAX * 100000);
        this->left = nullptr;
        this->right = nullptr;
        this->parent = nullptr;
    }
};

class BinarySearchTree {
public:
    Node* root;

    BinarySearchTree() {
        this->root = nullptr;
    }

    void insert(Node* node) {
        Node* y = nullptr;
        Node* x = this->root;
        while (x != nullptr) {
            y = x;
            if (node->ts < x->ts) {
                x = x->left;
            } else {
                x = x->right;
            }
        }
        node->parent = y;
        if (y == nullptr) {
            this->root = node;
        } else if (node->ts < y->ts) {
            y->left = node;
        } else {
            y->right = node;
        }
    }

    Node* search(int key) {
        Node* x = this->root;
        while (x != nullptr && key != x->ts) {
            if (key < x->ts) {
                x = x->left;
            } else {
                x = x->right;
            }
        }
        return x;
    }

    void inorder_print(Node* root) {
        if (root != nullptr) {
            inorder_print(root->left);
            cout << root->ts << " ";
            inorder_print(root->right);
        }
    }

    void left_rotate(Node* x) {
        //TODO
    }

    void right_rotate(Node* y) {
        //TODO
    }

    int minimum(Node* x) {
        while (x->left != nullptr) {
            x = x->left;
        }
        return x->ts;
    }

    int maximum(Node* x) {
        while (x->right != nullptr) {
            x = x->right;
        }
        return x->ts;
    }

    int successor(Node* x) {
        //TODO

    }

    int predecessor(Node* x) {
        //TODO

    }

    void fixup_insert(Node* z) {
        //TODO

    }

    int search_or_sum(int ts1, int ts2) {
        //TODO

    }

    int sum_values_between(Node* node, int ts1, int ts2) {
        //TODO

    }
};

int main() {

    return 0;
}
