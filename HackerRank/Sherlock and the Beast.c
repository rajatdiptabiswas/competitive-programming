#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    int t; 
    scanf("%d",&t);

	//start:
    for (int a0 = 0; a0 < t; a0++)
    {
        int n; 
        scanf("%d",&n);

        int i, j;
        //int looprun = 0;
        int flag = 0;
        
        for (i = (n / 3); i >= 0; --i)
        {
            for (j = 0; j <= (n / 3); ++j)
            {	
            	//looprun++;
            				
				//printf("%d\n", looprun);
				//printf("i = %d | j = %d\n", i, j);
            	
                if (((3*i) + (5*j)) == n)
                {
                    //printf("Condition met | i = %d | j = %d\n", i, j);

                    for (int k = 0; k < 3*i; ++k)
                    {
                        printf("5");
                    }

                    for (int k = 0; k < 5*j; ++k)
                    {
                        printf("3");
                    }

                    printf("\n");
					
					flag = 1;
					
					break;
                    //goto start;
                }

                if (i == 0 && j == (n/3))
                {
                    printf("-1\n");
					
					flag = 1;
					
					break;
                    //goto start;
                }
            }
            
            if (flag == 1)
            {
            	break;
			}
			
			else
				continue;
            
        }
    }
    
    return 0;
}
