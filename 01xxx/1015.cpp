#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> used_index;

int find_element_index(vector<int> vec, int element) {
    for (int i = 0; i < vec.size(); i++) {
        if (vec[i] == element) {
            auto it = find(used_index.begin(), used_index.end(), i);
            if (it == used_index.end()) {
                used_index.push_back(i);
                return i;
            }
        }
    }
}

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    vector<int> A_sort = A;
    sort(A_sort.begin(), A_sort.end());
    for (int i = 0; i < N; i++) {
        cout << find_element_index(A_sort, A[i]) << " ";
    }
}