#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; ++i)
	{
		unsigned int n;
		scanf("%u", &n);

		printf("%u\n", ~n);
	}

	return 0;
}