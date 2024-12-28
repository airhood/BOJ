#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Node {
public:
    int num;
    Node* parent;
    vector<Node*> childs;

    void AddChild(Node* child) {
        child->parent = this;
        childs.push_back(child);
    }

    Node* GetChild(int num) {
        if (childs.size() == 0) return nullptr;

        for (int i = 0; i < childs.size(); i++) {
            if (childs[i]->num == num) return childs[i];
        }
        for (int i = 0; i < childs.size(); i++) {
            auto result = childs[i]->GetChild(num);
            if (result != nullptr) return result;
        }
        return nullptr;
    }

    void RemoveChild(int num) {
        childs.erase(remove_if(childs.begin(), childs.end(), [num](auto x) -> bool { return (x->num == num); }), childs.end());
    }

    int CountLeafNodes() {
        if (childs.size() == 0) return 1;

        int count = 0;
        for (int i = 0; i < childs.size(); i++) {
            count += childs[i]->CountLeafNodes();
        }
        return count;
    }
};

// TODO: Unsolved

int main() {
    int N;
    cin >> N;
    Node* root = new Node;
    for (int i = 0; i < N; i++) {
        int parent;
        cin >> parent;
        if (parent == -1) {
            root->num = i;
            root->parent = nullptr;
            continue;
        }
        Node* newNode = new Node;
        newNode->num = i;
        if (parent == 0) {
            root->AddChild(newNode);
            continue;
        }
        root->GetChild(parent)->AddChild(newNode);
    }
    int del;
    cin >> del;
    
    if (del == 0) {
        cout << 0;
        return 0;
    }
    root->GetChild(del)->parent->RemoveChild(del);
    cout << root->CountLeafNodes();
}