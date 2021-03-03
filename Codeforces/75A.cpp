#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#define lli long long int
using namespace std;


lli stringToInt(string& s) {
    lli ans = 0;
    for (char c : s) {
        ans *= 10;
        ans += c - '0';
    }
    return ans;
}

void removeZero(string& s){
    s.erase(remove(s.begin(), s.end(), '0'), s.end());
}

int main(int argc, char const *argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    lli a, b, c;
    cin >> a >> b;
    c = a + b;

    string aStr = to_string(a), bStr = to_string(b), cStr = to_string(c);
    removeZero(aStr), removeZero(bStr), removeZero(cStr);

    if (stringToInt(aStr) + stringToInt(bStr) == stringToInt(cStr)) {
        cout << "YES";
    } else {
        cout << "NO";
    }
    cout << endl;
    
    return 0;
}