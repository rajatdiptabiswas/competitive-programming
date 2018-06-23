#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n, k;
	scanf("%d", &n);
	scanf("%d", &k);

	int* cloud = (int*) malloc (sizeof(int) * n); //int cloud[n];

	for (int x = 0; x < n; ++x)
	{
		scanf("%d", &cloud[x]);
	}

	// for (int x = 0; x < n; ++x)
	// {
	// 	printf("%d", cloud[x]);
	// }

	int energy = 100;
    
	for (int i = 0; i < n; i = i + k)
	{
		if (cloud[i] == 1)
		{
			energy = energy - 2;
		}

		energy--;
	}

	printf("%d\n", energy);

	return 0;
}

