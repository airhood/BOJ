#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> baskets(N);
    for (int m = 0; m < M; m++) {
        int i, j, k;
        cin >> i >> j >> k;
        for (int a = i; a <= j; a++) {
            baskets[a-1] = k;
        }
    }

    for (int i = 0; i < N; i++) {
        cout << baskets[i] << " ";
    }
}