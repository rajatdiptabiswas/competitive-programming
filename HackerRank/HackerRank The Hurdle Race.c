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
	int k; 
	scanf("%d %d",&n,&k);
	
	int max = 0;

	int *height = malloc(sizeof(int) * n);
	for(int height_i = 0; height_i < n; height_i++)
	{
		scanf("%d",&height[height_i]);

		if (max < height[height_i])
		{
			max = height[height_i];	
		}
	}
    
	if(k >= max)
		printf("0\n");
	else
		printf("%i\n", max - k);

	return 0;
}
