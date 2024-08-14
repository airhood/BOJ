#include <iostream>

using namespace std;

int main() {
    int test_cases;
    cin >> test_cases;
    for (int i = 0; i < test_cases; i++) {
        int x1, y1, r1, x2, y2, r2;
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        int distance_sq = (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2);
        int r_add_sq = (r1+r2) * (r1+r2);
        int r_sub_sq = (r1-r2) * (r1-r2);
        
        if (distance_sq == 0) {
            if (r_sub_sq == 0) cout << "-1" << endl;
            else cout << "0" << endl;
        }
        else if (distance_sq > r_add_sq) cout << "0" << endl;
        else if (distance_sq == r_add_sq) cout << "1" << endl;
        else if (distance_sq == r_sub_sq) cout << "1" << endl;
        else if ((distance_sq > r_sub_sq) && (distance_sq < r_add_sq)) cout << "2" << endl;
        else cout << "0" << endl;
    }
}