#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main() {
    int N;
    cin >> N;

    int* count = new int[10];
    for (int i = 0; i < 10; i++) {
        count[i] = 0;
    }

    int add = 0;
    for (int i = 0; N != 0; i++) {
        int current_digit = N % 10;
        N /= 10;

        count[0] -= pow(10, i);
        for (int j = 0; j < current_digit; j++) {
            count[j] += (N + 1) * pow(10, i);
        }
        count[current_digit] += N * pow(10, i) + 1 + add;
        for (int j = current_digit + 1; j <= 9; j++) {
            count[j] += N * pow(10, i);
        }

        add += current_digit * pow(10, i);
    }

    for (int i = 0; i < 10; i++) {
        cout << count[i] << " ";
    }
}