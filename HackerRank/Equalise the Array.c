#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);

	int a[n];
	int count[101] = {0};

	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &a[i]);

		count[a[i]]++;
	}

	int maxcount = 0;

	for (int i = 0; i < 101; ++i)
	{
		//printf("count[%d] = %d\n", i, count[i]);

		if (maxcount <= count[i])
		{
			maxcount = count[i];
		}
		
		//printf("maxcount = %d\n", maxcount);
	}

	printf("%d\n", (n - maxcount));

	return 0;
}
