#include <iostream>
using namespace std;

int arr[10002];

int main() {
    int M, N, min_v, result = 0;
    for (int i = 0; i <= 100; ++i) {
        arr[i * i] = 1;
    }
    cin >> M;
    cin >> N;
    for (int j = M; j <= N; ++j) {
        if (arr[j] == 1) {
            if (result == 0) {
                min_v = j;
                result += j;
            } else result += j;
        }
    }
    if (result == 0) cout << -1;
    else cout << result << "\n" << min_v;
    return 0;
}