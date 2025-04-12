#include <iostream>
#include <string>
#include <regex>

using namespace std;

int main() {
    string str;
    cin >> str;

    regex regex("(100+1+|01)+");
    bool result = regex_match(str, regex);
    if (result) cout << "SUBMARINE";
    else cout << "NOISE";
}