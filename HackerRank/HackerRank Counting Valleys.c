#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);

	int level = 0;
	int mountain = 0;
	int valley = 0;

	char lvl[n];
	scanf("%s", lvl);

	for (int i = 0; i < n; i++)
	{
		if (lvl[i] == 'U')
			level++;
		else if (lvl[i] == 'D')
			level--;

		if ((level == 1) && (lvl[i + 1] == 'D'))
			mountain++;
		else if ((level == -1) && (lvl[i + 1] == 'U'))
			valley++;
	}
	
	printf("%i\n", valley);

	return 0;
}
