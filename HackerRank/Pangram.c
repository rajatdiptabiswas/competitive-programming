#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() 
{
	char* s = (char*)malloc(1000 * sizeof(char));
	scanf("%[^\n]s", s);

	int len = strlen(s);

	// printf("len = %d\n", len);

    for (int i = 0; i < 26; i++)
    {
    	for (int j = 0; j < len; ++j)
    	{
    		// printf("i = %c | j = %d\n", 97+i, j);

    		if (s[j] == 32)
    			continue;

    		if (s[j] == 97+i || s[j] == 65+i)
    			break;

    		if (j == len-1)
    		{
    			printf("not pangram\n");
    			
    			return 0;
    		}
    	}
    }

    printf("pangram\n");

    return 0;
}

