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
    int t; 
    scanf("%d %d", &n, &t);
    
    int width[n];
    
    for(int width_i = 0; width_i < n; width_i++)
    {
       scanf("%d", &width[width_i]);
    }
    
    for(int a0 = 0; a0 < t; a0++)
    {
        int i; 
        int j; 
        scanf("%d %d", &i, &j);

        int max = 3;

        for (int x = i; x <= j; ++x)
        {
            if (width[x] < max)
            {
                max = width[x];
            }
        }

        printf("%d\n", max);
    }
    
    return 0;
}
