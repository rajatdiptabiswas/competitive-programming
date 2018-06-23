#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int getTotalX(int a_size, int* a, int b_size, int* b)
{
    int max = (*(a+(a_size - 1)) > *(b+(b_size - 1))) ? *(a+(a_size - 1)) : *(b+(b_size - 1));

    int count = 0;
    
    int x;
    for(x = 2; x <= max; x++)
    {
    	int bool_a = 0;
    	int bool_b = 0;
    	
    	for(int a_i = 0; a_i < a_size; a_i++)
    	{
       		if ((x % a[a_i]) == 0)
       		{	
       			bool_a = 1;
       			continue;
       		}

       		else
       		{
       			bool_a = 0;
       			break;
       		}
    	}
    	
    	for(int b_i = 0; b_i < b_size; b_i++)
    	{
       		if ((b[b_i] % x) == 0)
       		{
       			bool_b = 1;
       			continue;
       		}

       		else
       		{
       			bool_b = 0;
       			break;
       		}
    	}
    	
    	if (bool_a == 1 && bool_b == 1)
    		count++;
    }

    return count;
}

int main() 
{
    int n; 
    int m; 
    scanf("%d %d", &n, &m);
    
    int *a = malloc(sizeof(int) * n);
    for(int a_i = 0; a_i < n; a_i++)
    {
       scanf("%d",&a[a_i]);
    }
    
    int *b = malloc(sizeof(int) * m);
    for(int b_i = 0; b_i < m; b_i++)
    {
       scanf("%d",&b[b_i]);
    }
    
    int total = getTotalX(n, a, m, b);
    
    printf("%d\n", total);
    
    return 0;
}
