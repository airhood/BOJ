#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define ITERATE(var, init, N) for (int var = init; var < N; var++)

int main() {
    int N;
    cin >> N;

    int score = 0;
    int strike = 0;

    ITERATE(i, 0, N) {
        int input;
        cin >> input;
        
        if (input == 1) {
            strike++;
            score += strike;
        }
        else {
            strike = 0;
        }
    }

    cout << score;
}