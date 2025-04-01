#include <iostream>
#include <set>

using namespace std;

int main() {
    set<int> set;

    for (int i = 0; i < 10; i++) {
        int temp;
        cin >> temp;
        set.insert(temp % 42);
    }

    cout << set.size();
}