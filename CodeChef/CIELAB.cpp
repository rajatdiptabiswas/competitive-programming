#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char const *argv[])
{
	long long int a, b;
	cin >> a >> b;

	long long int c = a - b;

	if (c % 10 == 9)
	{
		c--;
	}
	else
	{
		c++;
	}

	cout << c << endl;

	return 0;
}