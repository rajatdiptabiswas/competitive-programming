#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int run;
	scanf("%d", &run);

	long int n, a, b;
	for (int i = 0; i < run; ++i)
	{
		scanf("%ld%ld%ld", &n, &a, &b);
        
        if (a > b)
            a ^= b ^= a ^= b;

        long int prevans = 0;

		for (int i = 0; i < n; ++i)
		{
			long int ans = ((n - i - 1) * a) + (i  * b);

			if (ans == prevans)
				break;
			else
				printf("%ld ", ans);

			prevans = ans;
		}
        
        printf("\n");
	}

	return 0;
}