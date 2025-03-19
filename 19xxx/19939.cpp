#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

#define ITERATE(var, init, N) for (int var = init; var < N; var++)

int main() {
    int N, K;
    cin >> N >> K;

    int defaultNum = K * (K + 1) / 2;

    if (defaultNum > N) {
        cout << -1;
        return 0;
    }

    N -= defaultNum;

    int add = N / K;
    int lack = N % K;

    int result;
    if (lack != 0) {
        result = (K - 1) + 1;
    }
    else {
        result = (K - 1);
    }

    cout << result;
}