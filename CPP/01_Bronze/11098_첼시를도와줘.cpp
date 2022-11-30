#include <iostream>
#include <string>
using namespace std;

int main() {
    int TC, n, t;
    string str;

    cin >> TC;
    for (int i = 0; i < TC; ++i) {
        cin >> n;
        int max_v = 0;
        string v_str;
        for (int j = 0; j < n; ++j) {
            cin >> t >> str;
            if (max_v < t) {
                max_v = t;
                v_str = str;
            }
        }
        cout << v_str << endl;
    }
    return 0;
}