#include <iostream>
#include <vector>

using namespace std;

int min(int a, int b) {
    if (a >= b) return b;
    else return a;
}

int min(int a, int b, int c) {
    return min(min(a, b), c);
}

const int A_cost = 3;
const int B_cost = 5;
const int C_cost = 7;

int main() {
    int N;
    cin >> N;

    vector<int> list(N);
    for (int i = 0; i < N; i++) {
        cin >> list[i];
    }

    auto buy_A = [&list](int i, int k) {
        list[i] -= k;
    };

    auto buy_B = [&list](int i, int k) {
        list[i] -= k;
        list[i + 1] -= k;;
    };

    auto buy_C = [&list](int i, int k) {
        list[i] -= k;;
        list[i + 1] -= k;;
        list[i + 2] -= k;;
    };

    int money = 0;
    int i = 0;
    while (i < N) {
        if (i < N - 2) {
            if ((list[i] != 0) && (list[i + 1] != 0) && (list[i + 2] != 0)) {
                if (list[i + 1] > list[i + 2]) {
                    int buy_amount = min(list[i + 1] - list[i + 2], list[i]);
                    buy_B(i, buy_amount);
                    money += buy_amount * B_cost;
                }
                else {
                    int buy_amount = min(list[i], list[i + 1], list[i + 2]);
                    buy_C(i, buy_amount);
                    money += buy_amount * C_cost;
                }
            }
            else if ((list[i] != 0) && (list[i + 1] != 0)) {
                int buy_amount = min(list[i], list[i + 1]);
                buy_B(i, buy_amount);
                money += buy_amount * B_cost;
            }
            else if (list[i] != 0) {
                int buy_amount = list[i];
                buy_A(i, buy_amount);   
                money += buy_amount * A_cost;
            }
        }
        else if (i < N - 1) {
            if ((list[i] != 0) && (list[i + 1] != 0)) {
                int buy_amount = min(list[i], list[i + 1]);
                buy_B(i, buy_amount);
                money += buy_amount * B_cost;
            }
            else if (list[i] != 0) {
                int buy_amount = list[i];
                buy_A(i, buy_amount);
                money += buy_amount * A_cost;
            }
        }
        else {
            if (list[i] != 0) {
                int buy_amount = list[i];
                buy_A(i, buy_amount);
                money += buy_amount * A_cost;
            }
        }

        if (list[i] == 0) i++;
    }

    cout << money;
}