#include <iostream>
#include <string>
using namespace std;

int main() {
    int TC, d, m, y, dd = 100, mm = 100, yy = 3000, DD = 0, MM = 0, YY = 0;
    cin >> TC;
    string name, max_n, min_n;
    for (int i = 0; i < TC; i++) {
        cin >> name >> d >> m >> y;
        if (YY < y) {
            YY = y;
            MM = m;
            DD = d;
            min_n = name;
        } else if (YY == y) {
            if (MM < m) {
                MM = m;
                DD = d;
                min_n = name;
            } else if (MM == m) {
                if (DD < d) {
                    DD = d;
                    min_n = name;
                }
            }
        } if (yy > y) {
            yy = y;
            mm = m;
            dd = d;
            max_n = name;
        } else if (yy == y) {
            if (mm > m) {
                mm = m;
                dd = d;
                max_n = name;
            } else if (mm == m) {
                if (dd > d) {
                    dd = d;
                    max_n = name;
                }
            }
        }
    }
    cout << min_n << "\n" << max_n;
    return 0;
}