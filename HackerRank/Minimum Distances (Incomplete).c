#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
	int n; 
	scanf("%d",&n);

	int *A = malloc(sizeof(int) * n);

	int dist[n/2];
	int x = 0;

	for(int i = 0; i < n; i++)
	{
		scanf("%d",&A[i]);
	}

	for(int i = 0; i < n; i++)
	{
		for(int j = i+1; j < n; j++)
		{
			if(A[i] == A[j])
			{
				dist[x] = j - i;
    			//printf("dist[%d] = %d\n", x, j-i);
				x++;
    			//printf("x = %d\n", x);
    			//printf("Condition met\n");
			}
		}
	}

	if(x == 0)
	{
		printf("-1\n");
	}

	else
	{
		int min = dist[0];

		for(int i = 1; i <= x; i++)
		{
			if (min > dist[i])
			{
				min = dist[i];
    			//printf("Minimum changed\n");
			}
		}

		printf("%d\n", min);
	}

	return 0;
}