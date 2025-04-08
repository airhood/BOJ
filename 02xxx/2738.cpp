#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<int>> list1(N);
    vector<vector<int>> list2(N);

    for (int i = 0; i < N; i++) {
        list1[i] = vector<int>(M);
        for (int j = 0; j < M; j++) {
            cin >> list1[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        list2[i] = vector<int>(M);
        for (int j = 0; j < M; j++) {
            cin >> list2[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << list1[i][j] + list2[i][j] << " ";
        }
        cout << endl;
    }
}