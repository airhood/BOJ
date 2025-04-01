#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; i++) {
        int R;
        string str;
        cin >> R >> str;
        
        for (int j = 0; j < str.length(); j++) {
            for (int k = 0; k < R; k++) cout << str[j];
        }
        
        cout << endl;
    }
}