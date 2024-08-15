#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> height_list(9);
    int sum = 0;

    for (int i = 0; i < 9; i++) {
        cin >> height_list[i];
        sum += height_list[i];
    }

    for (int i = 0; i < 8; i++) {
        for (int j = i + 1; j < 9; j++) {
            if ((100 + height_list[i] + height_list[j]) == sum) {
                height_list.erase(height_list.begin() + i);
                height_list.erase(height_list.begin() + j - 1); // i가 j 앞에 있기 때문에 i가 삭제되면 요소들이 1칸씩 앞으로 밀림
                goto done;
            }
        }
    }

    done:

    sort(height_list.begin(), height_list.end());

    for (int i = 0; i < 7; i++) {
        cout << height_list[i] << endl;
    }
}