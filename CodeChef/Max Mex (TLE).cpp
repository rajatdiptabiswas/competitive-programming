#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <set>
using namespace std;

int calculateMex(set<int> Set)
{
    int Mex = 0;
 
    while (Set.find(Mex) != Set.end())
        Mex++;
 
    return (Mex);
}

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;

	while(t--)
	{
		set<int> intSet;

		int n, k;
		cin >> n;
		cin >> k;

		while(n--)
		{
			int input;
			cin >> input;

			intSet.insert(input);
		}

		// cout << "\nThe elements in the ordered set are:\n";
		// set<int> :: iterator itr;
		// for (itr = intSet.begin(); itr != intSet.end(); ++itr)
		// {
		// 	cout << (*itr) << endl;
		// }

		// cout << "\nMex value is: ";
		// cout << calculateMex(intSet) << endl;

		int max = *intSet.rbegin();
		int ans = calculateMex(intSet);

		// cout << "max = " << max << endl;

		for (int i = 0; i < k; ++i)
		{
			intSet.insert(calculateMex(intSet));
			max = *intSet.rbegin();
			ans = calculateMex(intSet);
			
			if(ans > max)
			{
				ans = max + k;
				break;
			}	
		}

		cout << ans << endl;
	}

	return 0;
}