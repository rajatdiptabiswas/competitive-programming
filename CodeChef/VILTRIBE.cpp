// #include <stdio.h>
// #include <string.h>
#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	// scanf("%d", &t);
	cin >> t;

	while (t--)
	{
		// char str[100000];
		string str;
		cin >> str;

		int a_count = 0, b_count = 0;
		int prev_index;

		char prev = '.';

		for (int i = 0; i < str.length(); ++i)
		{
			if (str[i] == 'A')
			{
				if (prev == 'A')
				{
					a_count += i - prev_index;
					prev_index = i;
					continue;
				}

				else if (prev == 'B')
				{
					a_count++;
					prev_index = i;
					prev = 'A';
					continue;
				}

				a_count++;
				prev = 'A';
				prev_index = i;
			}
			
			else if (str[i] == 'B')
			{
				if (prev == 'B')
				{
					b_count += i - prev_index;
					prev_index = i;
					continue;
				}

				else if (prev == 'A')
				{
					b_count++;
					prev_index = i;
					prev = 'B';
					continue;
				}

				b_count++;
				prev = 'B';
				prev_index = i;
			}
		}

		printf("%d %d\n", a_count, b_count);
	}
	
	return 0;
}