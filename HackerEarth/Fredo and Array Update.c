#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int n;
	scanf("%d", &n);

	int array[n];

	long int sum = 0;

	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &array[i]);
		
		sum += array[i];
	}

	int ans = sum/n;

	if((n * ans) <= sum)
		ans++;

	printf("%d\n", ans);

	return 0;
}