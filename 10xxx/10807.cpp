#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, V;
    cin >> N;
    vector<int> list(N);
    for (int i = 0; i < N; i++) {
        cin >> list[i];
    }
    cin >> V;
    int count = 0;
    for (int i = 0; i < N; i++) {
        if (list[i] == V) count++;
    }
    cout << count;
}