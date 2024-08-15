#include <iostream>

using namespace std;

int main() {
    int h, m;
    int t;
    cin >> h >> m;
    cin >> t;
    int k = m + t;
    h += k / 60;
    m = k % 60;

    if (h >= 24) h = h - 24;

    cout << h << " " << m;
}