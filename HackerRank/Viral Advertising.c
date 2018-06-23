#include <stdio.h>
#include <math.h>

int main()
{
	int n;
	scanf("%d", &n);

	int people = 5;
	int totallike = 0;

	for (int i = 1; i <= n; ++i)
	{
		int like = floor(people / 2);

		if (n != 1)
		{
			people = like * 3;
		}

		totallike = totallike + like;
	}

	printf("%d\n", totallike);

	return 0;
}
