#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);

	int a[n+1];
	int z;

	for (int i = 1; i <= n; ++i)
	{
		scanf("%d", &z);

		a[i] = z;
	}

	int x = 1;
	int y;

	for (int i = 1; i <= n; ++i)
	{
		for (y = 1; y <= n; ++y)
		{
			if (a[a[y]] == x)
			{
				printf("%d\n", y);
				break;
			}
		}

		x++;
	}

	return 0;
}