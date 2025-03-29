#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    string str;
    cin >> N;
    cin >> str;

    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += str[i] - '0';
    }

    cout << sum;
}