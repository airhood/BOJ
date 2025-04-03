#include <iostream>

using namespace std;

int main() {
	int t;
	string str;
	int score;
	int strike;

	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> str;
		
		score = 0;
		strike = 1;

		for (int i = 0; i < str.length(); i++) {
			if (str[i] == 'O') score += strike++;
			else if (str[i] == 'X') strike = 1;
		}

		cout << score << '\n';
	}
}