#include <iostream>

using namespace std;

int main() {
    int N, arr[101], result = 0;
    cin >> N;
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }
    for (int i = 0; i < N; ++i) {
        if (arr[i] != 1) {
            int cnt = 0;
            for (int j = 1; j < arr[i]; ++j) {
                if (arr[i] % j == 0) cnt += 1;
                if (cnt == 2) break;
            }
            if (cnt == 1) result += 1;
        }
    }
    cout << result;
}