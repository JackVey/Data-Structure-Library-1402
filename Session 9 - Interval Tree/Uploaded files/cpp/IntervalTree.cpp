#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <chrono>
#include <ctime>
#include <fstream>
#include <sstream>

using namespace std;

struct Interval {
    double low, high;
};

struct Node {
    Interval i;
    double max;
    Node* left;
    Node* right;
};

Node* newNode(const Interval& i) {
    Node* temp = new Node;
    temp->i = i;
    temp->max = i.high;
    temp->left = nullptr;
    temp->right = nullptr;
    return temp;
}

Node* insert(Node* root, const Interval& i) {
    //TODO
}

bool doOverlap(const Interval& i1, const Interval& i2) {
    if (i1.low <= i2.high && i2.low <= i1.high)
        return true;

    return false;
}

Node* overlapSearch(Node* root, const Interval& i) {
    //TODO
}

Node* leftMostSearch(Node* root, const Interval& i) {
    //TODO
}

Node* findMin(Node* node) {
    while (node->left != nullptr)
        node = node->left;
    return node;
}

Node* successor(Node* root, const Interval& i) {
    Node* current = nullptr;
    Node* successor = nullptr;

    while (root != nullptr) {
        if (root->i.low > i.low) {
            successor = root;
            root = root->left;
        } else if (root->i.low < i.low) {
            root = root->right;
        } else {
            if (root->right != nullptr) {
                successor = findMin(root->right);
            }
            break;
        }
    }

    return successor;
}
