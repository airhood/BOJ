#include <iostream>
#include <vector>

using namespace std;

// 피사노 주기: 1,500,000
const int D = 1000000;
const int pisano_period = 1500000; // = 1.5 x D

int main() {
    long long n;
    cin >> n;

    if (n == 0) {
        cout << 0;
        return 0;
    }

    vector<int> fibo(n%pisano_period + 1);
    fibo[0] = 0;
    fibo[1] = 1;
    for (int i = 2; i <= n%pisano_period; i++) {
        fibo[i] = (fibo[i-1] + fibo[i-2]) % D;
    }

    cout << fibo.back();
}