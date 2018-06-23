#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);

	int a[n];

	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &a[i]);
	}

	int flag = 1;

	while(flag == 1)
	{
		flag = 0;

		int count = 0;
		int min = 1000;

		for (int i = 0; i < n; ++i)
		{
			if (a[i] == 0)
				continue;

			else 
			{
				if (a[i] < min)
				{
					min = a[i];
				}
			}
		}

		for (int i = 0; i < n; ++i)
		{
			if (a[i] != 0)
			{
				a[i] = a[i] - min;
				count++;
				flag = 1;
			}
		}

		if (count != 0)
			printf("%d\n", count);
	}
	
	return 0;
}