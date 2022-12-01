#include <iostream>

using namespace std;

int arr[10002];

int main() {
    int M, N, sum = 0, min = -1;
    cin >> M >> N;

    for (int i = M; i <= N; i++) {
        for (int div = 1; div <= i; div++) {
            if (i % div == 0)
                arr[i] += 1;
        }
        if (arr[i] == 2) {
            if (min == -1)
                min = i;
            sum += i;
        }
    }
    if (min == -1)
        cout << -1 << '\n';
    else
        cout << sum << '\n' << min << '\n';
}