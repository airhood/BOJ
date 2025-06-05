#include <iostream>
#include <vector>

using namespace std;

vector<int> parents;
vector<vector<int>> childrens;

void del(int index) {
    for (auto& child : childrens[index]) {
        del(child);
    }
    childrens[index].clear();
    childrens[index].push_back(-1); // 해당 node는 사라졌음을 의미
}

int main() {
    int N;
    cin >> N;

    parents = vector<int>(N);
    childrens = vector<vector<int>>(N);

    for (int i = 0; i < N; i++) cin >> parents[i];

    int del_index;
    cin >> del_index;

    for (int i = 0; i < N; i++) {
        if (parents[i] == -1) continue;
        childrens[parents[i]].push_back(i);
    }

    del(del_index);
    childrens[parents[del_index]].pop_back(); // 개수만 따지기에 아무 원소나 삭제

    int leaf_count = 0;
    for (int i = 0; i < N; i++) {
        if (childrens[i].size() == 0) leaf_count++;
    }

    cout << leaf_count;
}