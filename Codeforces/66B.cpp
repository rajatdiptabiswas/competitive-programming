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
#define MP make_pair
#define PB push_back
#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int uint64;
using namespace std;


int main(int argc, char const *argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, a;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    int maxValue = 0;
    for (int i = 0; i < v.size(); i++) {
        int l = i - 1;
        int leftValue = 0;
        while (l >= 0) {
            if (v[l] <= v[l + 1]) {
                leftValue++;
            } else {
                break;
            }
            l--;
        }

        int r = i + 1;
        int rightValue = 0;
        while (r < v.size()) {
            if (v[r - 1] >= v[r]) {
                rightValue++;
            } else {
                break;
            }
            r++;
        }

        maxValue = max(maxValue, leftValue + rightValue + 1);
    }

    cout << maxValue << endl;
    
    return 0;
}