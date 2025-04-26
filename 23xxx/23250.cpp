#include <iostream>

using namespace std;

int main() {
    long long N, K;
    cin >> N >> K;

    long long A = ((K & (K - 1)) % 3) + 1;
    long long B = (((K | (K - 1)) + 1) % 3) + 1;

    if (N % 2 == 0) {
        if (A == 2) A = 3;
        else if (A == 3) A = 2;
        
        if (B == 2) B = 3;
        else if (B == 3) B = 2;
    }

    cout << A << " " << B;
}