#include <iostream>
#include <string>

using namespace std;


int main() {
	string str;

	cin >> str;

	for (char i = 'a'; i <= 'z'; i++) {
		cout << (int)str.find(i) << ' ';
	}
}