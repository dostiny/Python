#include <iostream>
using namespace std;

int main() {
    int n, x = 0, y = 0;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        x = i;
        y = n - i;
        for (int j = 0; j < x; ++j) cout << ' ';
        for (int k = 0; k < y; ++k) cout << '*';
        cout << '\n';
    }
    return 0;
}