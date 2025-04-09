#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> list(N);
    for (int i = 0; i < N; i++) cin >> list[i];

    if (N == 1) {
        cout << "A";
        return 0;
    }
    else if (N == 2) {
        if (list[0] == list[1]) cout << list[0];
        else cout << "A";
        return 0;
    }
    else {
        int a;
        if (list[1] - list[0] == 0) a = 0;
        else {
            a = (list[2] - list[1]) / (list[1] - list[0]);
        }

        int b = list[1] - list[0] * a;

        for (int i = 1; i < N; i++) {
            if (list[i] != list[i - 1] * a + b) {
                cout << "B";
                return 0;
            }
        }

        cout << list[N - 1] * a + b;
    }
}