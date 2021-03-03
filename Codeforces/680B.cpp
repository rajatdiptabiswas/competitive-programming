#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <limits>
#include <string>
#include <iterator>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#define lli long long int
using namespace std;


int main(int argc, char const *argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    lli n, a, e;
    cin >> n >> a;
    vector<int> input(n + 1);
    for (int i = 1; i < n + 1; i++) {
        cin >> e;
        input[i] = e;
    }

    lli l = a - 1, r = a + 1, total = input[a];
    
    int lValue, rValue;
    while (1 <= l || r <= n) {
        lValue = (l >= 1) ? input[l] : 1;
        rValue = (r <= n) ? input[r] : 1;
        if (lValue & rValue) {
            if (1 <= l && r <= n) {
                total += 2;
            } else {
                total += 1;
            }
        }
        l--, r++;
    }

    cout << total << endl;
    
    return 0;
}