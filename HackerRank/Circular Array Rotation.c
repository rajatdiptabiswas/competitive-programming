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
    int q; 
    scanf("%d %d %d", &n, &k, &q);
    
    int *a = malloc(sizeof(int) * n);
    
    for (int a_i = 0; a_i < n; a_i++)
    {
     scanf("%d", &a[a_i]);
    }

    for (int i = 0; i < k; ++i)
    {
        int temp = a[n-1];

        //printf("temp = %d\n", temp);

        for (int j = 1; j < n; ++j)
        {
            a[n-j] = a[n-j-1];
        }

        a[0] = temp;
    }

    for (int a0 = 0; a0 < q; a0++)
    {	
        int m; 
        scanf("%d", &m);

        printf("%d\n", a[m]);
    }

    return 0;
}
