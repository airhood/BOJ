#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<double> list(N);

    for (int i = 0; i < N; i++) {
        cin >> list[i];
    }

    double max = list[0];
    for (int i = 1; i < N; i++) {
        if (list[i - 1] > 1) {
            list[i] = list[i] * list[i - 1];
        }

        if (list[i] > max) max = list[i];
    }

    cout << fixed, cout.precision(3);
    cout << max;
}