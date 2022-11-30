#include <iostream>

using namespace std;

int main() {
    int n1, n2, tem, n3, n4, result;
    cin >> n1 >> n2;
    n3 = n1; n4 = n2;
    while (n2 != 0) {
        tem = n2;
        n2 = n1 % n2;
        n1 = tem;
    }
    result = (n3 * n4) / n1;
    cout << n1 << "\n" << result;
    return 0;
}