#include <stdio.h>

int  main()
{
	int n, p;
	scanf("%d%d", &n, &p);

	if((n-p) == 1 && p != 1)
	{
		if(p % 2 == 0) //p even
			printf("0\n");
		else //p odd
			printf("1\n");
	}
	else
		((n-p)/2) < ((p-0)/2) ? printf("%d\n", ((n-p)/2)) : printf("%d\n", ((p-0)/2));

	return 0;
}