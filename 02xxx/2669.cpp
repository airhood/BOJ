#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<vector<int>> coord(100);
    for (int x = 0; x < 100; x++) {
        coord[x] = vector<int>(100);
        for (int y = 0; y < 100; y++) {
            coord[x][y] = 0;
        }
    }

    for (int i = 0; i < 4; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        for (int x = x1; x < x2; x++) {
            for (int y = y1; y < y2; y++) {
                coord[x-1][y-1] = 1;
            }
        }
    }

    int count = 0;
    for (int x = 0; x < 100; x++) {
        for (int y = 0; y < 100; y++) {
            if (coord[x][y] == 1) count++;
        }
    }

    cout << count;
}