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
    
    // char* *grid = malloc(sizeof(char*) * n);
    // for(int grid_i = 0; grid_i < n; grid_i++)
    // {
    //    grid[grid_i] = (char *)malloc(10240 * sizeof(char));
    //    scanf("%s",grid[grid_i]);
    // }

    int a[n][n];

    for (int i = 0; i < n; ++i)
    {
    	for (int j = 0; j < n; ++j)
    	{
    		scanf("%d", &a[i][j]);
    	}
    }

    for (int i = 0; i < n; ++i)
    {
    	for (int j = 0; i < n; ++j)
    	{
    		if (a[i-1][j] < a[i][j] && a[i+1][j] < a[i][j] && a[i][j-1] < a[i][j] && a[i][j+1] < a[i][j])
    			printf("X");
    		else
    			printf("%d", a[i][j]);
    	}

    	printf("\n");
    }
    return 0;
}
