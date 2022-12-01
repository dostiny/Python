#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, arr[100000], sum_n;
    cin >> n;
    for (int i = 0; i < n; ++i) cin >> arr[i];
    cin >> sum_n;
    sort(arr, arr + n);
    int hap, left = 0, right = n - 1, cnt = 0;
    while (left != right) {
        hap = arr[left] + arr[right];
        if (sum_n == hap) {
            cnt += 1;
            left += 1;
        } else if (sum_n > hap) {
            left += 1;
        } else if (sum_n < hap) {
            right -= 1;
        }
    }
    cout << cnt << '\n';
    return 0;
}