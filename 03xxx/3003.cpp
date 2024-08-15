#include <iostream>

using namespace std;

int main() {
    int king, queen, rook, bishop, kight, pawn;
    cin >> king >> queen >> rook >> bishop >> kight >> pawn;
    cout << 1-king << " " << 1-queen << " " << 2-rook << " " << 2-bishop << " " << 2-kight << " " << 8-pawn;
}