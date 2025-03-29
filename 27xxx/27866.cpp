#include <iostream>
#include <string>

using namespace std;

int main() {
    string str;
    int pos;
    cin >> str;
    cin >> pos;
    cout << str[pos - 1];
}