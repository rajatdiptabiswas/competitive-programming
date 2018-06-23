#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int reversed(int x)
{
    int rev = 0;
    
    while (x != 0)
    {
    	rev = (10 * rev) + (x % 10);
    	x = x / 10;
    }

    return rev;
}

int main() 
{
	int i, j, k;
	scanf("%d%d%d", &i, &j, &k);
    
	int beautiful = 0;

    int a;
	for (a = i; a <= j; a++)
	{
		if (((abs(a - reversed(a))) % 6)  == 0)
			beautiful++;
	}

	printf("%d\n", beautiful);

    return 0;
}
