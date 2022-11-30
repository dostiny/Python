#include <iostream>
using namespace std;

int main() {
    int M, D, ans = 0;
    cin >> M;
    cin >> D;
    if (M == 2) {
        if (D == 18) ans = 3;
        else if (D < 18) ans = 1;
        else if (D > 18) ans = 2;
    } else if (M < 2) ans = 1;
        else if (M > 2) ans = 2;

    if (ans == 1) cout << "Before";
    else if (ans == 2) cout << "After";
    else if (ans == 3) cout << "Special";
    return 0;
}