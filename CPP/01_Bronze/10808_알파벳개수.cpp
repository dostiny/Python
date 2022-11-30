#include <iostream>
using namespace std;

int alpa[26];

int main() {
    for (int i = 0; i < 26; ++i) {
        alpa[i] = 0;
    }
    string str = "abcdefghijklmnopqrstuvwxyz";
    int n;
    string inputstr;
    cin >> inputstr;
    for (int i = 0; i < inputstr.length(); ++i) {
        n = str.find(inputstr[i]);
        alpa[n] += 1;
    }
    for (int i = 0; i < 26; ++i) {
        cout << alpa[i] << ' ';
    }
    return 0;
}