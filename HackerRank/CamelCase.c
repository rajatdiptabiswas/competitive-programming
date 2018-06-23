#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    char* s = (char *)malloc(100240 * sizeof(char));
    scanf("%s", s);

    int word = 1;

    for (int i = 0; s[i] != '\0'; ++i)
    {
    	if (s[i] >= 65  && s[i] <= 90)
    		word++;
    }

    printf("%d\n", word);
    
    return 0;
}

