#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int A, B, C;
    cin >> A >> B >> C;

    int num = A * B * C;
    string str = to_string(num);

    vector<int> list(10);
    for (int i = 0; i < 10; i++) list[i] = 0;

    for (int i = 0; i < str.length(); i++) {
        list[str[i] - '0']++;
    }

    for (int i = 0; i < 10; i++) cout << list[i] << endl;
}