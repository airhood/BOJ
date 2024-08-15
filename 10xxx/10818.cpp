#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    int min, max = 0;
    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;
        if (min == 0) min = num;
        if (max == 0) max = num;
        if (num < min) min = num;
        if (num > max) max = num;
    }

    cout << min << " " << max;
}