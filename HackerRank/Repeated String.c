#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    char* s = (char *)malloc(512000 * sizeof(char));
    scanf("%s", s);
    
    long n; 
    scanf("%ld",&n);
    
    int length = 0;
    int a_count = 0;

    for (int i = 0; s[i] != '\0'; ++i)
    {
    	length++;

    	//printf("length = %d\n", length);

    	if (s[i] == 'a')
    	{
    		a_count++;

    		//printf("a count = %d\n", a_count);
    	}
    }

    long int result = ((n/length) * a_count);

    //printf("initial result = %ld\n", result);

    for (int i = 0; i < (n%length); ++i)
    {
    	if (s[i] == 'a')
    	{
    		result++;

    		//printf("Result incremented");
    	}
    }

    printf("%ld\n", result);

    return 0;
}

