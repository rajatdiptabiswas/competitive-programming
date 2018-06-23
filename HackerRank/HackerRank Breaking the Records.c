#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

// int* getRecord(int s_size, int* s, int *result_size)
// {
//     // Complete this function
// }

int main() 
{
   int n; 
   scanf("%d",&n);
   
   int *s = malloc(sizeof(int) * n);
   for(int s_i = 0; s_i < n; s_i++)
   {
      scanf("%d",&s[s_i]);
   }

   int max = s[0];
   int min = s[0];

   int maxcount = 0;
   int mincount = 0;

   int x;

   for(x = 0; x < n; x++)
   {
   	if(max < s[x])
   	{
   		maxcount++;
   		max = s[x];
   	}

   	if(min > s[x])
   	{
   		mincount++;
   		min = s[x];
   	}
   }

   printf("%d %d", maxcount, mincount);
   
   // int result_size;
   // int* result = getRecord(n, s, &result_size);
   // for(int i = 0; i < result_size; i++) 
   // {
   //     if (i) 
   //     {
   //         printf(" ");
   //     }
   //     printf("%d", result[i]);
   // }
   // puts("");
   
   return 0;
}