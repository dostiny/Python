#include <iostream>
using namespace std;

int main() {
    int N, arr[100], num, cnt = 0;
    cin >> N;
    for (int i = 0; i < N; ++i) cin >> arr[i];
    cin >> num;
    for (int j = 0; j < N; ++j) {
        if (arr[j] == num) {
            cnt += 1;
        }
    }
    cout << cnt << "\n";
    return 0;
}