#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int min(int a, int b) {
    if (a >= b) return b;
    else return a;
}

int make_num(int a, int b, int c, int d) {
    return 1000 * a + 100 * b + 10 * c + d;
}

int find_num(int a, int b, int c, int d) {
    int x = make_num(a, b, c, d);
    int y = make_num(b, c, d, a);
    int z = make_num(c, d, a, b);
    int w = make_num(d, a, b, c);

    return min(min(x, y), min(z, w));
}

int main() {
    int a0, b0, c0, d0;
    cin >> a0 >> b0 >> c0 >> d0;

    int target_num = find_num(a0, b0, c0, d0);

    set<int> set;
    for (int a = 1; a <= 9; a++) {
        for (int b = 1; b <= 9; b++) {
            for (int c = 1; c <= 9; c++) {
                for (int d = 1; d <= 9; d++) {
                    int num = find_num(a, b, c, d);
                    set.insert(num);
                }
            }
        }
    }

    auto iter = set.find(target_num);
    int index = distance(set.begin(), iter);
    cout << index + 1;
}