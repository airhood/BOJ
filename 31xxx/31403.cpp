#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int A, B, C;
    cin >> A >> B >> C;

    int B_length = log10(B) + 1;

    int numerical_calculation = A + B - C;
    int string_calculation = (A * pow(10, B_length)) + B - C;

    cout << numerical_calculation << endl << string_calculation;
}