#include <iostream>
using namespace std;

int girl[6], boy[6];

int main() {
    int N, K, S, H, result = 0;
    cin >> N >> K;
    for (int i = 0; i < N; ++i) {
        cin >> S >> H;
        if (S == 0) {
            girl[H - 1] += 1;
            if (girl[H - 1] == K) {
                result += 1;
                girl[H - 1] = 0;
            }
        } else if (S == 1) {
            boy[H - 1] += 1;
            if (boy[H - 1] == K) {
                result += 1;
                boy[H -1] = 0;
            }
        }
    }
    for (int j = 0; j < 6; ++j) {
        if (girl[j] != 0) result += 1;
        if (boy[j] != 0) result += 1;
    }
    cout << result << endl;
    return 0;
}