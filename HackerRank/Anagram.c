#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int anagram(char* s, int l)
{
    int a = 0;

    if ((l % 2) != 0)
    {
        return (-1);
    }

    else
    {
        for (int i = 0; i < (l/2); ++i)
        {
            for (int j = (l/2); j < l; ++j)
            {
                if (s[i] == s[j])
                {
                    // printf("if condition met\n");

                    s[i] = '0';
                    s[j] = '0';
                    break;
                }

                else if (j == (l-1))
                {
                    a++;

                    // printf("a incremented\n");
                }
            }
        } 
    }

    return a;
    
}

int main() 
{
    int q; 
    scanf("%i", &q);
    
    for (int a0 = 0; a0 < q; a0++)
    {
        char* s = (char *)malloc(512000 * sizeof(char));
        scanf("%s", s);

        int len = 0;
        while (s[len] != '\0')
        {
            len++;
        }

        // printf("%d\n", len);
        
        int result = anagram(s, len);
        printf("%d\n", result);
    }
    
    return 0;
}
