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
    scanf("%d", &n);
    
    int *c = malloc(sizeof(int) * n);
    for(int c_i = 0; c_i < n; c_i++)
    {
       scanf("%d",&c[c_i]);
    }

    int *checked = calloc(n, sizeof(int));
    
	int pairs = 0;

    for(int i = 0; i < n; i++)
    {
    	int count = 0;

    	if(checked[i] == 0)
    	{
    		for(int j = 0; j < n; j++)
    		{
    			if(c[j] == c[i])
    			{
    				count++;
    				checked[j] = 1;
    			}
    		}
    	}

    	pairs += count/2;
    }

    printf("%d\n", pairs);
    
    return 0;
}
