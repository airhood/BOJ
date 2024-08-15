#include <iostream>
#include <vector>

using namespace std;

int main() {
    int max = 0;
    int max_index;
    vector<int> list(9);
    for (int i = 0; i < 9; i++) {
        cin >> list[i];
    }

    for (int i = 0; i < 9; i++) {
        if (list[i] > max) {
            max = list[i];
            max_index = i;
        }
    }

    cout << max << endl;
    cout << max_index + 1;
}