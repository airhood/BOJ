#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int H, W, N;
        cin >> H >> W >> N;
        int X = ((N - 1) / H) + 1;
        int Y = N % H;
        if (Y == 0) Y = H;
        cout << X + 100 * Y << endl;
    }
}