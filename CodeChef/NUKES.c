#include <stdio.h>
#include <stdlib.h>

int main()
{
	int a, n, k;
	scanf("%d %d %d", &a, &n, &k);
	
	n++;

	while (k--)
	{
		printf("%d ", a%n);
		a /= n;
	}	
}