#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    int *h = malloc(sizeof(int) * 26);
    
    for(int h_i = 0; h_i < 26; h_i++)
    {
       scanf("%d",&h[h_i]);
    }
    
    char* word = (char *)malloc(512000 * sizeof(char));
    scanf("%s", word);

    int max = 0;
    int count = 0;

    for(int i = 0; (*(word+i)) != '\0'; i++)
    {
    	if(max < h[(word[i]) - 97])
    		max = h[(word[i]) - 97];
    		
    	//debug
    	//printf("word[i] = %d\nh[word[i] - 97] = %d\n", word[i], h[(word[i]) - 97]);

    	count++;
    }

    int area = count * max * 1; //in mm^2

    printf("%d\n", area);
    
	//debug
	//printf("count = %d\nmax = %d\n", count, max);
    
    return 0;
}
