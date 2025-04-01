#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> list(8);
    for (int i = 0; i < 8; i++) cin >> list[i];

    bool pass = true;
    for (int i = 0; i < 8; i++) {
        if (list[i] != (i + 1)) {
            pass = false;
            break;
        }
    }

    if (pass) {
        cout << "ascending";
        return 0;
    }

    pass = true;
    for (int i = 0; i < 8; i++) {
        if (list[i] != (8 - i)) {
            pass = false;
            break;
        }
    }

    if (pass) {
        cout << "descending";
        return 0;
    }

    cout << "mixed";
}