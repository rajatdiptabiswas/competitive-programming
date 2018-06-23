#include <stdio.h>
#include <stdlib.h>

int main()
{
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++)
	{
		int n;
		scanf("%d", &n);

		int * a = (int *)malloc(n * sizeof(int));

		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &a[i]);
		}

		int min = a[0];

		for (int i = 1; i < n; ++i)
		{
			if (min > a[i])
			{
				min = a[i];
			}
		}

		int count = 0;

		for (int i = 0; i < n; ++i)
		{
			if (a[i] == min)
			{
				count++;
			}
		}

		if (count % 2 != 0)
			printf("Lucky\n");

		else
			printf("Unlucky\n");

		free(a);
	}

	return 0;
}