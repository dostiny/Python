#include <iostream>
using namespace std;

int num[10];

int main() {
    int N, i, max_n = 0;;

    cin >> N;
    while (N != 0) {
        i = N % 10;
        if (i == 6 || i == 9) {
            if (num[6] <= num[9]) num[6] += 1;
            else if (num[6] > num[9]) num[9] += 1;
        } else num[i] += 1;
        N = N / 10;
    }
    for (int j = 0; j < 10; ++j) {
        if (max_n < num[j]) max_n = num[j];
    }
    cout << max_n;
    return 0;
}
