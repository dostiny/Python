#include <iostream>
using namespace std;

int numli[10];

int main() {
    int A, B, C, mul;
    string mulst;
    cin >> A;
    cin >> B;
    cin >> C;
    mul = A * B * C;
    mulst = to_string(mul);

    for (int i = 0; i < mulst.length(); ++i) {
        char s = mulst[i] - '0';
        int n = s;
        numli[n] += 1;
    }
    for (int i = 0; i < 10; ++i) {
        cout << numli[i] << '\n';
    }
    return 0;
}