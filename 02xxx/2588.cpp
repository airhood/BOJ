#include <iostream>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    int a1 = a%10;
    int a2 = (a%100 - a1) / 10;
    int a3 = a / 100;
    int b1 = b%10;
    int b2 = (b%100 - b1) / 10;
    int b3 = b / 100;

    int r1 = (a1*b1) + (a2*b1*10) + (a3*b1*100);
    int r2 = (a1*b2) + (a2*b2*10) + (a3*b2*100);
    int r3 = (a1*b3) + (a2*b3*10) + (a3*b3*100);

    int r = r1 + (r2*10) + (r3 * 100);

    cout << r1 << endl;
    cout << r2 << endl;
    cout << r3 << endl;
    cout << r << endl;
}