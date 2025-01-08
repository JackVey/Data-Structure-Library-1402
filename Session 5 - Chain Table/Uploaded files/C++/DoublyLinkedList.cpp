#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node* prev;

	public:
	Node(int value){
		data = value;
		next = NULL;
		prev = NULL;
	}
};

class DoublyLinkedList{
public:
	Node* head = NULL;
	Node* tail = NULL;

	public:
	void insertBefore(Node* y, Node* x){
		// TODO
	}

	public:
	void insertTail(Node* x){
		if (tail == NULL){
			head = x;
			tail = x;
		}else{
			tail->next = x;
			x->prev = tail;
			tail = x;
		}
	}

	public:
	void insertKeepSorted(Node* x){
		Node* p = head;
		while(p != NULL && p->data < x->data){
			p = p ->next;
		}
		if (p == NULL){
			insertTail(x);
		}else{
			insertBefore(p, x);
		}
	}

	public:
	Node* search(int value){
		Node* node = head;
		while (node != NULL){
			if (node->data == value){
				break;
			}
			node = node->next;
		}
		return node;
	}

	public:
	void remove(Node* node){
		if (head == NULL || node == NULL){
			return;
		}

		if (head == node){
			head = node->next;
			head->prev=NULL;
		}

		if (tail == node){
			tail = node->prev;
			tail->next=NULL;
		}

		if (node->next != NULL){
			node->next->prev = node->prev;
		}

		if (node->prev != NULL){
			node->prev->next = node->next;
		}
	}
};

int main(int argc, char const *argv[])
{
	// TODO
	return 0;
}